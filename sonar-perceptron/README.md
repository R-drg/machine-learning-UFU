# Sonar Perceptron

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
para o classificar sinais de um sonar

Base de dados:

-UCI - Machine Learning Repository (sonar.csv)
-Número de atributos: 60
-Número de medidas:208

> https://archive.ics.uci.edu/ml/datasets/Connectionist+Bench+(Sonar,+Mines+vs.+Rocks)

## Desenvolvimento

Utilizando o código abaixo desenvolvido em python foi realizado o treino através do algoritmo de Retropropagação]

Função para leitura do dataset

```python
def read_training():
    testingset=open("testingset","r")
    for line in testingset:
        floats =[]
        line1= line[:(len(line)-3)]
        numbers=line1.split(",")
        if (len(numbers)>1):
            for number in numbers:
                floats.append(float(number))
            if(len(floats)!=0):
                teste_entrada.append(floats)
        line2= line[len(line)-2:len(line)-1]
        if(line2=='M'):
            teste_saida.append(1.0)
        elif(line2 =='R'):
            teste_saida.append(0.0)
```

Função de treinamento do neurônio
```python
while ciclo<numCiclo and erroQ>erroMin:
    erroQ=0
    ciclo=ciclo+1

    ##########FEED FOWARD
    #Passo4
    for i in range(len(x)):
        for j in range(neuroniosescondidos):
            sum_k=0
            for u in range(neuroniosentrada):
                sum_k=sum_k+x[i][u]*v[j][u]
            zin[j]=sum_k+bv[j]
            z[j]= (2/(1+math.exp(-zin[j])))-1
    #Passo5
        sum_i=0
        for j in range(neuroniosescondidos):
            sum_i=z[j]*w[j][0]+sum_i
        yin=sum_i+bw[0]
        y=(2/(1+np.exp(-yin)))-1

    ##################### FASE DE RETROPROPAGAÇÃO

        deltinhaw = (t[i] - y)*0.5*(1+y)*(1-y)
        deltabw=alfa*deltinhaw
        for j in range(neuroniosescondidos):
            deltaw[j]=alfa*deltinhaw*z[j]
            deltinhav[j]=deltinhaw*w[j]*0.5*(1+z[j])*(1-z[j])
            deltabv[j] = alfa * deltinhav[j][0]
            for k in range(neuroniosentrada):
                deltav[j][k]=alfa*deltinhav[j][0]*x[i][k]
                v[j][k]=v[j][k]+deltav[j][k]    
            bv[j] = bv[j]+deltabv[j]
        w=w+deltaw
        bw=bw+deltabw
   
    erroQ = erroQ + 0.5*((t[i]-y)*(t[i]-y))
    print("\nCiclo "+ str(ciclo) + ": "+ str(erroQ))
print("Fim do Treinamento\n"+
      "Erro Quadrático final: " + str(erroQ) + "\n" +
      "Ciclos: " + str(ciclo))
```

## Resultado

 Para os resultados a seguir, utilizei como parâmetro 4
neurônios escondidos, Taxa de apredizagem igual a 0.1, Erro total admissível igual a
0.0001 e um número máximo de 1000 ciclos.


```
Fim do Treinamento
Erro Quadrático f i n a l : 6.020501604037226 e−05
Ciclos : 188

TAXA DE ACERTO: 71/84 (85%)
```
