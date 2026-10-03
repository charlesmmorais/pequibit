# Fontes e dúvidas

- [Instalação oficial](https://quantum.cloud.ibm.com/docs/en/guides/install-qiskit).
- [Statevector](https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.quantum_info.Statevector).
- [Circuitos no Qiskit 2.2](https://quantum.cloud.ibm.com/docs/en/api/qiskit/2.2/circuit).
- [Transpilação e representação de computadores](https://quantum.cloud.ibm.com/docs/en/guides/represent-quantum-computers).
- [Grover](https://quantum.cloud.ibm.com/docs/en/tutorials/grovers-algorithm).

**Não encontrou Qiskit?** Confira se `python -m pip show qiskit` usa o mesmo ambiente do comando que executa o exemplo.

**Instalação falhou?** Confira internet, Python 3.12 e ambiente virtual. Registre a mensagem de erro em uma issue; não troque versões aleatoriamente antes de entender a causa.

**O estado equivalente tem sinal diferente?** Pode ser fase global. Compare com `Statevector.equiv`, em vez de exigir igualdade literal dos coeficientes.

**Posso inserir measure_all antes de calcular Statevector?** Não neste caminho de simulação unitária. Para os exemplos da trilha, obtenha o vetor e use `sample_counts`. Medição intermediária requer outra estratégia de execução.

**Posso usar direto na Tang Nano?** Não. As aulas reúnem uma referência de software para verificar o futuro executor; a integração com a placa ainda será construída.

Texto original do Pequibit; não há afiliação com IBM ou Sipeed.
