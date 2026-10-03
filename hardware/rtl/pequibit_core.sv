// Núcleo educativo de DOIS qubits. Não contém pinagem, UART ou clock de placa.
// Aceita um comando quando start=1 e busy=0. Executa no próximo clock.
// Comandos durante busy são ignorados. done/error são pulsos de um ciclo.
module pequibit_core (
    input  wire clk,
    input  wire rst,                  // reset síncrono, ativo em 1
    input  wire start,
    input  wire [2:0] opcode,         // 0 INIT, 1 H, 2 X, 3 Z, 4 CX, 5 LOAD
    input  wire target,
    input  wire control,
    input  wire [1:0] load_addr,
    input  wire signed [15:0] load_real,
    input  wire signed [15:0] load_imag,
    output reg busy,
    output reg done,
    output reg error,
    input  wire [1:0] read_addr,
    output wire signed [15:0] read_real,
    output wire signed [15:0] read_imag
);
    localparam [2:0] OP_INIT=0, OP_H=1, OP_X=2, OP_Z=3, OP_CX=4, OP_LOAD=5;
    reg signed [15:0] state_real [0:3];
    reg signed [15:0] state_imag [0:3];
    reg [2:0] active_op;
    reg active_target, active_control;
    reg [1:0] active_addr;
    reg signed [15:0] active_real, active_imag;

    // Pares do alvo q0: (0,1),(2,3). Pares de q1: (0,2),(1,3).
    wire [1:0] first_b = active_target ? 2'd2 : 2'd1;
    wire [1:0] second_a = active_target ? 2'd1 : 2'd2;
    wire signed [31:0] h0r, h1r, h2r, h3r;
    wire signed [31:0] h0i, h1i, h2i, h3i;
    q14_hadamard hr0(state_real[0], state_real[first_b], h0r, h1r);
    q14_hadamard hr1(state_real[second_a], state_real[3], h2r, h3r);
    q14_hadamard hi0(state_imag[0], state_imag[first_b], h0i, h1i);
    q14_hadamard hi1(state_imag[second_a], state_imag[3], h2i, h3i);

    reg signed [31:0] next_real [0:3];
    reg signed [31:0] next_imag [0:3];
    reg invalid;
    integer k, source;
    always @* begin
        invalid = 0;
        source = 0;
        for (k=0; k<4; k=k+1) begin
            next_real[k] = {{16{state_real[k][15]}}, state_real[k]};
            next_imag[k] = {{16{state_imag[k][15]}}, state_imag[k]};
        end
        case (active_op)
            OP_INIT: begin
                for (k=0; k<4; k=k+1) begin
                    next_real[k] = (k==0) ? 32'sd16384 : 32'sd0;
                    next_imag[k] = 0;
                end
            end
            OP_H: begin
                next_real[0]=h0r; next_imag[0]=h0i;
                next_real[first_b]=h1r; next_imag[first_b]=h1i;
                next_real[second_a]=h2r; next_imag[second_a]=h2i;
                next_real[3]=h3r; next_imag[3]=h3i;
            end
            OP_X, OP_CX: begin
                if (active_op==OP_CX && active_control==active_target)
                    invalid = 1;
                for (k=0; k<4; k=k+1) begin
                    source = k;
                    if (active_op==OP_X || ((k >> active_control) & 1))
                        source = k ^ (1 << active_target);
                    next_real[k] = {{16{state_real[source][15]}}, state_real[source]};
                    next_imag[k] = {{16{state_imag[source][15]}}, state_imag[source]};
                end
            end
            OP_Z: begin
                for (k=0; k<4; k=k+1)
                    if ((k >> active_target) & 1) begin
                        next_real[k] = -$signed({{16{state_real[k][15]}}, state_real[k]});
                        next_imag[k] = -$signed({{16{state_imag[k][15]}}, state_imag[k]});
                    end
            end
            OP_LOAD: begin
                // Ferramenta de preparação/depuração: não normaliza o estado.
                next_real[active_addr] = {{16{active_real[15]}}, active_real};
                next_imag[active_addr] = {{16{active_imag[15]}}, active_imag};
            end
            default: invalid = 1;
        endcase
        for (k=0; k<4; k=k+1)
            if (next_real[k] > 32'sd32767 || next_real[k] < -32'sd32768 ||
                next_imag[k] > 32'sd32767 || next_imag[k] < -32'sd32768)
                invalid = 1;
    end

    assign read_real = state_real[read_addr];
    assign read_imag = state_imag[read_addr];
    integer j;
    always @(posedge clk) begin
        if (rst) begin
            busy<=0; done<=0; error<=0;
            active_op<=OP_INIT; active_target<=0; active_control<=0;
            active_addr<=0; active_real<=0; active_imag<=0;
            for (j=0; j<4; j=j+1) begin
                state_real[j] <= (j==0) ? 16'sd16384 : 16'sd0;
                state_imag[j] <= 0;
            end
        end else begin
            done<=0; error<=0;
            if (busy) begin
                busy<=0; done<=1; error<=invalid;
                // Atomicidade: um erro preserva TODAS as amplitudes anteriores.
                if (!invalid)
                    for (j=0; j<4; j=j+1) begin
                        state_real[j]<=next_real[j][15:0];
                        state_imag[j]<=next_imag[j][15:0];
                    end
            end else if (start) begin
                active_op<=opcode; active_target<=target; active_control<=control;
                active_addr<=load_addr; active_real<=load_real; active_imag<=load_imag;
                busy<=1;
            end
        end
    end
endmodule
