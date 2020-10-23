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

## Desenvolvimento

No código escrito em python, primeiro, pede-se ao usuário sober a arquitetura da rede neural, podendo definir a quantidade de camadas escondidas. em seguida, realiza-se o treinamento atráves da seguinte função que retorna os pesos atualizados

```python
def treinamento_multilayer_perceptron(x,t,v,w,bv,bw,neuronios):
    alfa=float(input("\nTaxa de aprendizagem: "))
    erroMin=float(input("\nErro total admissivel: "))
    max_ciclos=int(input("\nNumero de Ciclos maximo:"))
    deltinha_v = z_in = z = delta_w = delta_bv = np.zeros(neuronios['escondidos'])
    delta_v = np.zeros((neuronios['entrada'],neuronios['escondidos']))
    deltinha_w=0
    ciclo=0
    erroQ=10
    while ciclo<max_ciclos and erroQ>erroMin:
        erroQ=0
        ciclo=ciclo+1
        for i in range(4):
            for j in range(neuronios['escondidos']):
                z_in[j]=x[i][0]*v[0][j] + x[i][1]*v[1][j] + bv[j]
                z[j]= (2/(1+np.exp(-z_in[j])))-1
            y_in=np.sum(z*w)+bw
            y=(2/(1+np.exp(-y_in)))-1
    
        ############ FASE DE RETROPROPAGAÇÃO

        deltinha_w = (t[i] - y)*0.5*(1+y)*(1-y)

        for j in range(neuronios['escondidos']):
            delta_w[j]=alfa*deltinha_w*z[j]

        delta_bw=alfa*deltinha_w

        for j in range(neuronios['escondidos']):
            deltinha_v[j]=deltinha_w*w[j]*0.5*(1+z[j])*(1-z[j])

        for j in range(neuronios['entrada']):
            for k in range(neuronios['escondidos']):
                delta_v[j][k]=alfa*deltinha_v[k][0]*x[i][j]

        for j in range(neuronios['escondidos']):
            delta_bv[j] = alfa * deltinha_v[j][0]

        w=w+delta_w
        bw=bw+delta_bw

        for j in range(neuronios['entrada']):
            for k in range(neuronios['escondidos']):
                v[j][k]=v[j][k]+delta_v[j][k]

        for j in range(neuronios['escondidos']):
            bv[j] = bv[j]+delta_bv[j]

        erroQ = erroQ + 0.5*((t[i]-y)*(t[i]-y))
    return v,w,bv,bw
```
Em seguida é feita a avaliação dos pesoss encontrados

```python
def validacao(x,t,v,w,bv,bw,hl):
    z = z_in=np.zeros(hl)
    print("\n\n TESTE DO TREINAMENTO\n\n")
    for i in range(4):
        for j in range(neuronios['escondidos']):
            z_in[j]=x[i][0]*v[0][j] + x[i][1]*v[1][j] + bv[j]
            z[j]= (2/(1+np.exp(-z_in[j])))-1
        y_in=np.sum(z*w)+bw
        y=(2/(1+np.exp(-y_in)))-1
        print("Target: " + str(t[i]) +"   Rede Treinada: " + str(y))
```

## Resultado
Para esses testes foi utilizado a seguinte arquitetura da rede neural, com 2 camadas  de entrada, 4 camadas escondidas e uma camada de saída
<img src="https://github.com/R-drg/machine-learning-UFU/blob/main/multilayer-perceptron/imagens/nn.png?raw=true" width="600">

Output da rede neural treinada
```
 TESTE DO TREINAMENTO


Target: -1.0   Rede Treinada: -0.9942180569524774
Target: 1.0   Rede Treinada: 0.9949568801745756
Target: 1.0   Rede Treinada: 0.9940582161797071
Target: -1.0   Rede Treinada: -0.9955280995244702
```
<img src="https://github.com/R-drg/machine-learning-UFU/blob/main/multilayer-perceptron/imagens/xor.jpg?raw=true">

## Conclusão

Pode-se concluir que o algoritmo de Retropropagação obteve sucesso ao ser treinado com
xor, o que algoritmos anteriores demonstravam dificuldade. Isso se deve as multicamadas
de neurônios
