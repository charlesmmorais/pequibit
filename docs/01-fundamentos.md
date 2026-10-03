# Antes do circuito: o que estamos representando?

## Um qubit

Um estado puro de um qubit é |ψ⟩ = α|0⟩ + β|1⟩. As amplitudes α e β são números complexos, e |α|² + |β|² = 1. Ao medir na base computacional, as probabilidades são |α|² e |β|².

Uma amplitude não é uma probabilidade. Ela pode ser negativa ou complexa; sua fase faz diferença quando caminhos interferem. Dizer apenas “50% de zero e 50% de um” perde parte da informação do estado.

## A experiência que muda a intuição

A porta H transforma |0⟩ em (|0⟩ + |1⟩)/√2. Aplicando H novamente, obtemos |0⟩. Se fossem apenas dois sorteios independentes, esse retorno determinístico não seria explicado. O cancelamento de amplitudes é a interferência.

Para cada par de amplitudes a e b, H calcula:

- a' = (a + b)/√2;
- b' = (a − b)/√2.

## Dois qubits

Guardamos quatro amplitudes, na ordem |00⟩, |01⟩, |10⟩, |11⟩. O qubit 0 é o bit menos significativo, à direita na escrita do estado. O índice inteiro da memória usa essa mesma convenção.

O estado (|00⟩ + |11⟩)/√2 é entrelaçado: não pode ser escrito como produto de dois estados individuais. Na FPGA, isso é uma propriedade do vetor simulado, não um fenômeno quântico físico no silício.

Só observar 00 e 11 não demonstra entrelaçamento: uma mistura clássica também produz essas contagens. Por isso estudaremos amplitudes e medições em outras bases.

## O custo de simular

Um vetor de estado de n qubits contém 2^n amplitudes. Dobrar o número de qubits não dobra a memória: cada qubit adicional já dobra a memória. Outras técnicas podem explorar circuitos especiais; o Pequibit começa pelo método geral de vetor de estado.

## Medir e olhar a memória são coisas diferentes

No modelo, podemos listar todas as amplitudes para depuração. Isso não representa uma medição possível de um único sistema quântico real. O comando de amostragem do software também não altera o vetor: ele representa medições de várias preparações idênticas. Medição intermediária com colapso é oferecida separadamente pela API Python `measure`; veja o [módulo 5](../curso/modulos/05-medicao.md).

Referência conceitual: IBM Quantum Learning, nas [fontes](07-referencias.md).
