"""Bell local por padrão; --enviar submete um job real após confirmação."""
import argparse
from datetime import datetime, timezone
from getpass import getpass
import json
from pathlib import Path
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler


def circuit():
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure_all()
    return qc


def summarize(counts):
    total = sum(counts.values())
    if total <= 0:
        raise ValueError('Não há amostras para analisar.')
    return {'shots_observados': total, 'contagens': counts,
            'fracao_bits_iguais': (counts.get('00', 0) + counts.get('11', 0))/total}


def connect():
    from qiskit_ibm_runtime import QiskitRuntimeService
    # Entradas interativas: a chave não fica no código ou no histórico do shell.
    token = getpass('API key IBM (entrada oculta): ').strip()
    instance = input('CRN da instância Open Plan: ').strip()
    if not token or not instance.startswith('crn:'):
        raise ValueError('Informe a API key e copie o CRN completo da instância.')
    return QiskitRuntimeService(channel='ibm_quantum_platform', token=token, instance=instance)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--enviar', action='store_true')
    mode.add_argument('--job', help='Consulta um job existente; não envia outro.')
    parser.add_argument('--shots', type=int, default=1024)
    parser.add_argument('--saida', type=Path)
    args = parser.parse_args()
    if not 1 <= args.shots <= 4096:
        parser.error('Use de 1 a 4096 shots neste laboratório.')
    if args.saida and args.saida.exists():
        parser.error('O arquivo de saída já existe; escolha outro nome.')
    if not args.enviar and not args.job:
        result = StatevectorSampler(seed=42).run([circuit()], shots=args.shots).result()
        report = {'modo': 'simulacao_local', **summarize(result[0].data.meas.get_counts())}
    else:
        service = connect()
        if args.job:
            job = service.job(args.job)
            print('Status:', job.status())
            status = str(job.status()).upper().split('.')[-1]
            if status != 'DONE':
                print('Consulte Workloads para detalhes. Esta consulta não reenviou o circuito.')
                return
        else:
            from qiskit.transpiler import generate_preset_pass_manager
            from qiskit_ibm_runtime import SamplerV2
            backend = service.least_busy(operational=True, simulator=False, min_num_qubits=2)
            isa = generate_preset_pass_manager(optimization_level=1, backend=backend).run(circuit())
            print('QPU:', backend.name, '| shots:', args.shots)
            print('Confirme no painel que o CRN informado pertence ao Open Plan.')
            print('O script não verifica o plano pelo nome da instância.')
            if input('Digite ENVIAR OPEN para consumir tempo de QPU: ').strip() != 'ENVIAR OPEN':
                print('Envio cancelado. Nenhum job foi submetido.')
                return
            job = SamplerV2(mode=backend).run([isa], shots=args.shots)
            report = {'modo': 'job_submetido', 'job_id': job.job_id(),
                      'backend': backend.name, 'shots_solicitados': args.shots,
                      'instrucoes_isa': dict(isa.count_ops())}
            print('Job enviado:', job.job_id(), flush=True)
            print('Guarde esse ID. Use --job ID para consultar sem reenviar.')
            save(report, args.saida)
            return
        counts = job.result()[0].data.meas.get_counts()
        report = {'modo': 'resultado_qpu', 'job_id': job.job_id(),
                  'backend': job.backend().name, **summarize(counts)}
    save(report, args.saida)


def save(report, path):
    report['data_utc'] = datetime.now(timezone.utc).isoformat()
    payload = json.dumps(report, ensure_ascii=False, indent=2)
    print(payload)
    if path:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open('x', encoding='utf-8') as output:
            output.write(payload + '\n')


if __name__ == '__main__':
    main()
