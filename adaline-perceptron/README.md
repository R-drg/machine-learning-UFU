# Adaline-Perceptron

## Objetivo

Utilizando a base de dados abaixo, Treinar um Perceptron e obter os pesos e bia finais
plotar o gráfico da fronteira de separação. Depois com a mesma base de dados reinar um
Adaline e obter os pesos e bia finais e plotar um gráfico contendo a fronteira de separação.
E por fim experimentar diferentes valores de alfa e plotar o erro quadrático em tempo de
treinamento

|  s1 |  s2 | t  |
|:---:|:---:|----|
| 1.0 | 1.0 | 1  |
| 1.1 | 1.5 | 1  |
| 2.5 | 1.7 | -1 |
| 1.0 | 2.0 | 1  |
| 0.3 | 1.4 | 1  |
| 2.8 | 1.0 | -1 |
| 0.8 | 1.5 | 1  |
| 2.5 | 0.5 | -1 |
| 2.3 | 1.0 | -1 |
| 0.5 | 1.1 | 1  |
| 1.9 | 1.3 | -1 |
| 2.0 | 0.9 | -1 |
| 0.5 | 1.8 | 1  |
| 2.1 | 0.6 | -1 |

## Desenvolvimento
### Adaline
Pegando o código de python, foi primeiro criado listas contendo os *inputs* e *outputs* (source e target) dos nossos dados 
e em seguida a função utilizada para o treinamento do Adaline

```python
def treinamento_adaline(maxCiclos,alfa,t,s):
    wNovo=[0,0]
    #Inicializa pesos e bias aleatorio
    wAnterior=[random.uniform(-0.5,0.5),random.uniform(-0.5,0.5)]
    bAnterior=random.uniform(-0.5,0.5)
    ciclo=0
    while(ciclo<=maxCiclos):
        erroQ = 0
        print("\nCiclo "+str(ciclo)+" => ",end='')
        for i in range(14):
            #calcula o y liquido
            yLiquido = wAnterior[0]*s[i][0] + wAnterior[1]*s[i][1] + bAnterior
            #calcula o erro quadratico
            erroQ = erroQ + (t[i]-yLiquido)*(t[i]-yLiquido)
            #Ajutas pesos
            wNovo[0]= wAnterior[0] + alfa*(t[i]-yLiquido)*s[i][0]
            wAnterior[0] = wNovo[0]
            wNovo[1]= wAnterior[1] + alfa*(t[i]-yLiquido)*s[i][1]
            wAnterior[1] = wNovo[1]
            #Ajusta bias
            bNovo = bAnterior + alfa*(t[i]-yLiquido)
            bAnterior = bNovo
        ciclo+=1
        print("wnovo[0]:%.1f  wnovo[1]: %.1f  bnovo: %.1f  erroQ:%.1f" % (wNovo[0],wNovo[1],bNovo,erroQ));
    return wNovo,bNovo
```
Por fim há a função de ativação e validação do neuronio, que a partir da equação abaixo, 
obtemos o resultado do neuronio treinado e recebemos a comparação entre o resultado esperado e obtido

```python
def ativacao(w,b,t,s):
    teta = 0
    print("\n\nResultados:\n");
    for i in range(14):
        flag="[Fail]"
        yLiquido = w[0]*s[i][0]+ w[1]*s[i][1] + b
        if(yLiquido>=teta):
            y=1
        else:
            y=-1
        if(y==t[i]):
            flag="[Pass]"
        print("Caso[%i]: Expectativa: %.1f Resultado: %.1f %s" % (i,t[i],y,flag))
```
### Perceptron

Semelhante ao código do Adaline, contudo com mudanças na função do treinamento

```python
def treinamento_perceptron(maxCiclos,alfa,t,s):
    wNovo=[0,0]
    #Inicializa pesos e bias aleatorio
    wAnterior=[0,0]
    bAnterior=ciclo=teta=0
    trocou=1
    while(trocou==1):
        trocou = 0
        print("\nCiclo "+str(ciclo)+" => ",end='')
        for i in range(14):
            #calcula o y liquido
            yLiquido = wAnterior[0]*s[i][0] + wAnterior[1]*s[i][1] + bAnterior
            if yLiquido>=teta:
                y=1
            else:   
                y=-1

            if(y!=t[i]):
                    trocou=1;
                    for z in range(2):
                        wNovo[z]=wAnterior[z]+ alfa*s[i][z]*t[i]
                        wAnterior[z]=wNovo[z]
                    bNovo=bAnterior+ alfa*t[i]
                    bAnterior=bNovo
        ciclo+=1
        print("wnovo[0]:%.4f  wnovo[1]: %.4f  bnovo: %.4f" % (wNovo[0],wNovo[1],bNovo));
    return wNovo,bNovo
```

## Resultado
### Adaline

Erro quadrático

<img src="https://github.com/R-drg/machine-learning-UFU/blob/main/adaline-perceptron/imagens/errograph.jpg?raw=true">

Output do console utilizando 300 ciclos máximos e taxa de aprendizado (*alfa*) de 0.1
```
Pesos finais: [-1.2240755098155904, 0.05751183291781553] Bias final: 1.4977662030498653
Caso[0]: Expectativa: 1.0 Resultado: 1.0 [Pass]
Caso[1]: Expectativa: 1.0 Resultado: 1.0 [Pass]
Caso[2]: Expectativa: -1.0 Resultado: -1.0 [Pass]
Caso[3]: Expectativa: 1.0 Resultado: 1.0 [Pass]
Caso[4]: Expectativa: 1.0 Resultado: 1.0 [Pass]
Caso[5]: Expectativa: -1.0 Resultado: -1.0 [Pass]
Caso[6]: Expectativa: 1.0 Resultado: 1.0 [Pass]
Caso[7]: Expectativa: -1.0 Resultado: -1.0 [Pass]
Caso[8]: Expectativa: -1.0 Resultado: -1.0 [Pass]
Caso[9]: Expectativa: 1.0 Resultado: 1.0 [Pass]
Caso[10]: Expectativa: -1.0 Resultado: -1.0 [Pass]
Caso[11]: Expectativa: -1.0 Resultado: -1.0 [Pass]
Caso[12]: Expectativa: 1.0 Resultado: 1.0 [Pass]
Caso[13]: Expectativa: -1.0 Resultado: -1.0 [Pass]
```

Grafico representando a decision boundary do Adaline

<img src="https://github.com/R-drg/machine-learning-UFU/blob/main/adaline-perceptron/imagens/adalinegraph.jpg?raw=true">

### Perceptron

Output do console utilizando 300 ciclos máximos e taxa de aprendizado (*alfa*) de 0.1

```
Resultados:

Pesos finais: [-0.26, 0.22] Bias final: 0.1
Caso[0]: Expectativa: 1.0 Resultado: 1.0 [Pass]
Caso[1]: Expectativa: 1.0 Resultado: 1.0 [Pass]
Caso[2]: Expectativa: -1.0 Resultado: -1.0 [Pass]
Caso[3]: Expectativa: 1.0 Resultado: 1.0 [Pass]
Caso[4]: Expectativa: 1.0 Resultado: 1.0 [Pass]
Caso[5]: Expectativa: -1.0 Resultado: -1.0 [Pass]
Caso[6]: Expectativa: 1.0 Resultado: 1.0 [Pass]
Caso[7]: Expectativa: -1.0 Resultado: -1.0 [Pass]
Caso[8]: Expectativa: -1.0 Resultado: -1.0 [Pass]
Caso[9]: Expectativa: 1.0 Resultado: 1.0 [Pass]
Caso[10]: Expectativa: -1.0 Resultado: -1.0 [Pass]
Caso[11]: Expectativa: -1.0 Resultado: -1.0 [Pass]
Caso[12]: Expectativa: 1.0 Resultado: 1.0 [Pass]
Caso[13]: Expectativa: -1.0 Resultado: -1.0 [Pass]
```

Grafico representando a decision boundary do Perceptron

<img src="https://github.com/R-drg/machine-learning-UFU/blob/main/adaline-perceptron/imagens/perceptrongraph.jpg?raw=true">
