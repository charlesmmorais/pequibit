"""Testes offline: nunca conectam a uma conta IBM ou submetem jobs reais."""
import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch
from qiskit.primitives import StatevectorSampler
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2
from laboratorios.ibm.bell import circuit, main, summarize


class BellTests(unittest.TestCase):
    def test_local_distribution(self):
        result = StatevectorSampler(seed=42).run([circuit()], shots=1024).result()
        counts = result[0].data.meas.get_counts()
        self.assertEqual(set(counts), {'00', '11'})
        self.assertEqual(summarize(counts)['shots_observados'], 1024)
        self.assertEqual(summarize(counts)['fracao_bits_iguais'], 1)

    def test_default_mode_does_not_connect_and_saves(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder)/'result.json'
            with patch('sys.argv', ['bell', '--saida', str(path)]), patch('laboratorios.ibm.bell.connect') as connect, contextlib.redirect_stdout(io.StringIO()):
                main()
            connect.assert_not_called()
            self.assertEqual(json.loads(path.read_text())['modo'], 'simulacao_local')

    def test_cancel_does_not_submit(self):
        service = Mock()
        with patch('sys.argv', ['bell', '--enviar']), patch('laboratorios.ibm.bell.connect', return_value=service), patch('qiskit.transpiler.generate_preset_pass_manager'), patch('qiskit_ibm_runtime.SamplerV2') as sampler, patch('builtins.input', return_value='NAO'), contextlib.redirect_stdout(io.StringIO()):
            main()
        sampler.assert_not_called()

    def test_submit_only_once(self):
        service, sampler = Mock(), Mock()
        service.least_busy.return_value.name = 'qpu-teste-offline'
        sampler.return_value.run.return_value.job_id.return_value = 'job-teste-offline'
        pm = Mock()
        pm.return_value.run.return_value.count_ops.return_value = {'cx': 1, 'measure': 2}
        with patch('sys.argv', ['bell', '--enviar']), patch('laboratorios.ibm.bell.connect', return_value=service), patch('qiskit.transpiler.generate_preset_pass_manager', pm), patch('qiskit_ibm_runtime.SamplerV2', sampler), patch('builtins.input', return_value='ENVIAR OPEN'), contextlib.redirect_stdout(io.StringIO()):
            main()
        sampler.return_value.run.assert_called_once()

    def test_retrieve_does_not_submit(self):
        service = Mock()
        service.job.return_value.status.return_value = 'QUEUED'
        with patch('sys.argv', ['bell', '--job', 'known-id']), patch('laboratorios.ibm.bell.connect', return_value=service), patch('qiskit_ibm_runtime.SamplerV2') as sampler, contextlib.redirect_stdout(io.StringIO()):
            main()
        service.job.assert_called_once_with('known-id')
        sampler.assert_not_called()

    def test_api_signatures_and_invalid_shots(self):
        import inspect
        inspect.signature(QiskitRuntimeService).bind(channel='ibm_quantum_platform', token='fake', instance='crn:fake')
        inspect.signature(SamplerV2).bind(mode=Mock())
        with patch('sys.argv', ['bell', '--shots', '0']), contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
            main()
