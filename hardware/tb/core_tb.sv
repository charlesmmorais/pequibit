`timescale 1ns/1ps
module core_tb;
    reg clk=0;
    always #5 clk=~clk;
    reg rst=1, start=0;
    reg [2:0] opcode=0;
    reg target=0, control=0;
    reg [1:0] load_addr=0, read_addr=0;
    reg signed [15:0] load_real=0, load_imag=0;
    wire busy, done, error;
    wire signed [15:0] read_real, read_imag;
    pequibit_core dut(.*);
    integer fd, result, count=0, n;
    integer op, tg, ct, addr, lr, li, err;
    integer expected [0:7];
    reg [4095:0] vector_file;
    initial begin
        if (!$value$plusargs("VECTORS=%s", vector_file)) $fatal(1,"Falta +VECTORS");
        fd=$fopen(vector_file,"r");
        if (!fd) $fatal(1,"Não abriu vetores");
        repeat(2) @(negedge clk);
        rst=0;
        // Reset deve abortar um comando em andamento e restaurar |00>.
        start=1; opcode=2;
        @(negedge clk);
        if (!busy) $fatal(1,"Comando não foi aceito");
        rst=1; start=0;
        @(negedge clk);
        if (busy || done || error || read_real!==16'sd16384) $fatal(1,"Reset falhou");
        rst=0;
        while (!$feof(fd)) begin
            result=$fscanf(fd,"%d %d %d %d %d %d %d %d %d %d %d %d %d %d %d\n",
                op,tg,ct,addr,lr,li,err,expected[0],expected[1],expected[2],expected[3],
                expected[4],expected[5],expected[6],expected[7]);
            if (result!=15) $fatal(1,"Vetor incompleto: %0d campos",result);
            opcode=op; target=tg; control=ct; load_addr=addr;
            load_real=lr; load_imag=li; start=1;
            @(negedge clk);
            if (!busy || done || error) $fatal(1,"Handshake de aceite falhou");
            // Durante busy, alteramos todos os operandos e mantemos start=1.
            // O comando concorrente deve ser ignorado e os originais preservados.
            opcode=7; target=~target; control=~control; load_real=99; load_imag=-99;
            @(negedge clk);
            start=0;
            if (busy || !done || error!==err[0]) $fatal(1,"Conclusão/erro incorreto vetor %0d",count);
            for (n=0;n<4;n=n+1) begin
                read_addr=n;
                #1;
                if ($signed(read_real)!==expected[2*n] || $signed(read_imag)!==expected[2*n+1])
                    $fatal(1,"Vetor %0d addr %0d obtido (%0d,%0d) esperado (%0d,%0d)",
                           count,n,$signed(read_real),$signed(read_imag),expected[2*n],expected[2*n+1]);
            end
            @(negedge clk);
            if (done || error || busy) $fatal(1,"Sinais não voltaram ao repouso");
            count=count+1;
        end
        $fclose(fd);
        $display("PASS: %0d comandos comparados bit a bit; reset e handshake verificados",count);
        $finish;
    end
    initial begin
        #10000000;
        $fatal(1,"Timeout");
    end
endmodule
