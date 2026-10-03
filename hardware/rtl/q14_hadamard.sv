// Butterfly real em ponto fixo. Usado separadamente nas partes real e imaginária.
// Escala 2^14; 1/sqrt(2) aproximado por 11585/16384.
// Saídas ampliadas permitem que o chamador detecte overflow antes de escrever.
module q14_hadamard (
    input  wire signed [15:0] a,
    input  wire signed [15:0] b,
    output wire signed [31:0] out_a,
    output wire signed [31:0] out_b
);
    wire signed [16:0] sum_value = {a[15], a} + {b[15], b};
    wire signed [16:0] diff_value = {a[15], a} - {b[15], b};

    function automatic signed [31:0] scale_and_round;
        input signed [16:0] value;
        reg signed [31:0] product;
        begin
            product = value * 32'sd11585;
            // Arredondamento ao mais próximo; empate afasta de zero.
            if (product < 0)
                scale_and_round = -(((-product) + 32'sd8192) >>> 14);
            else
                scale_and_round = (product + 32'sd8192) >>> 14;
        end
    endfunction

    assign out_a = scale_and_round(sum_value);
    assign out_b = scale_and_round(diff_value);
endmodule
