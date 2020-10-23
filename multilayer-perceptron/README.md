# Multilayer Perceptron

## Introdução

### Pesos sinápticos

O primeiro passo do algoritmo de retropropagação é a inicialização dos pesos da rede.
Como normalmente não temos nenhuma informação sobre os pesos da rede, um método
muito utilizado é inicializar os pesos aleatoriamente, com distribuição uniforme sobre um
pequeno intervalo em torno do zero.

### Algoritmo de Retropropagação

O algoritmo de retropropagação de erro, é um algoritmo utilizado no treinamento de redes
neurais multicamadas, e consiste em dois passos de computação: o processamento direto
e o processamento reverso.
No processamento direto, uma entrada é aplicada à rede neural e seu efeito é propagado pela rede, camada a camada. Durante o processamento direto, os pesos da rede
permanecem fixos.
No processamento reverso, um sinal de erro calculado na saída da rede é propagado no
sentido reverso, camada a camada, e ao final deste processo os pesos são ajustados de
acordo com uma regra de correção de erro.
O algoritmo de retropropagação segue os seguintes passos:
1. Inicialização. Inicialize os pesos da rede aleatoriamente ou segundo algum método.
2. Processamento direto. Apresente um padrão à rede. Compute as ativações de todos
os neurônios da rede e então calcule o erro.
3. Passo reverso. Calcule os novos pesos para cada neurônio da rede, no sentido retroativo (isto é, da saída para a entrada), camada a camada.
4. Teste de parada. Teste o critério de parada adotado. Se satisfeito, termine o algoritmo;
5. senão volte ao passo 2.

## Objetivo

Treinar uma rede neural multicamada usando o algoritmo da retropropagação do erro
para o caso da função lógica Ou-exclusivo bipolar.

| x_1 | x_2 | T  |
|-----|-----|----|
| -1  | -1  | -1 |
| -1  | 1   | 1  |
| 1   | -1  | 1  |
| 1   | 1   | -1 |

+ Desenhar a arquitetura da rede neural (com neurônios de entrada, da camada de
saída e da camada escondida)
+ Plotar a curva do erro quadratico
+ Apresentar os pesos encontrados
