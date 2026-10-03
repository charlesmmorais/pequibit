"""Gera casos determinísticos e compara Icarus com o modelo inteiro."""
import random
import shutil
import subprocess
import tempfile
from pathlib import Path
from software.fixed_reference import FixedCore


def vectors():
    model, rows = FixedCore(), []

    def command(op, target=0, control=0, address=0, real=0, imag=0):
        error = model.execute(op, target, control, address, real, imag)
        rows.append([op, target, control, address, real, imag, int(error)]
                    + [component for pair in model.state for component in pair])

    # Bell e inversão, ambos os alvos e todas as entradas de base.
    for target in (0, 1):
        command(0)
        command(1, target)
        command(4, 1-target, target)
        assert model.state == [(11585, 0), (0, 0), (0, 0), (11585, 0)]
        command(4, 1-target, target)
        command(1, target)
    for basis in range(4):
        for target in (0, 1):
            for op in (1, 2, 3, 4):
                command(0)
                for bit in range(2):
                    if basis & (1 << bit):
                        command(2, bit)
                command(op, target, 1-target)
    # Entradas complexas e fronteiras que provocam overflow atômico.
    for pairs in [[(1000, -2000), (-3000, 4000), (5000, 6000), (-7000, -8000)],
                  [(8192, -8192), (0, 0), (0, 0), (0, 0)],
                  [(32767, 0)]*4, [(-32768, -32768)]*4]:
        for op in (1, 2, 3, 4):
            for target in (0, 1):
                command(0)
                for address, (real, imag) in enumerate(pairs):
                    command(5, address=address, real=real, imag=imag)
                command(op, target, 1-target)
    command(6)
    command(7)
    command(4, 0, 0)
    command(4, 1, 1)
    # Circuitos longos: inclui fase/sinal em ambos os componentes.
    rng = random.Random(2026)
    for _ in range(10):
        command(0)
        for _ in range(50):
            target = rng.randrange(2)
            command(rng.choice([1, 2, 3, 4]), target, 1-target)
    return rows


def main():
    for name in ('iverilog', 'vvp'):
        if not shutil.which(name):
            raise SystemExit(f'Instale {name} (pacote Icarus Verilog) para executar este teste.')
    root = Path(__file__).resolve().parents[2]
    rows = vectors()
    with tempfile.TemporaryDirectory(prefix='pequibit-rtl-') as folder:
        folder = Path(folder)
        data = folder/'vectors.txt'
        data.write_text('\n'.join(' '.join(map(str, row)) for row in rows)+'\n')
        binary = folder/'core.vvp'
        subprocess.run(['iverilog', '-g2012', '-s', 'core_tb', '-o', str(binary),
                        str(root/'hardware/rtl/q14_hadamard.sv'),
                        str(root/'hardware/rtl/pequibit_core.sv'),
                        str(root/'hardware/tb/core_tb.sv')], check=True)
        subprocess.run(['vvp', str(binary), f'+VECTORS={data}'], check=True, timeout=30)


if __name__ == '__main__':
    main()
