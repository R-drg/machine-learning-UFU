# Regra de Hebb

## Objetivo

Considerando as 16 funções lógicas que podem ser construidas a partir de 2 variáveis.
Mostrar que a regra de Hebb pode encontrar os pesos das redes neurais correspondentes
a 14 destas funções lógicas quando for usada a representação bipolar.

## Desenvolvimento

Pegando o código de python, criei primeiro uma função que retorna-se a lista *t* com todos resultados das 16 funções lógicas diferentes, que são do número binário 0001 até 1111

```python
def generate_tables():
    t=np.zeros((16,4))
    for i in range(16):
        num = i
        j=3
        while(j>=0):
            if(num%2==1):
                t[i][j]=1
            else:
                t[i][j]=0
            num=int(num/2)
            j-=1
    return t
```

Em seguida, criei uma função que realiza-se o treinamento de hebb, assimila-se os novos pesos e retorna-os

```python
def treinamento_hebb(t,s):
    wNovo=np.zeros((16,2))
    bNovo=np.zeros(16)
    for i in range(16):
        wAnterior=[0,0]
        bAnterior=0
        for j in range(4):
            for z in range(2):
                wNovo[i][z]=wAnterior[z]+s[j][z]*t[i][j]
                wAnterior[z]=wNovo[i][z]
            bNovo[i]=bAnterior+t[i][j]
            bAnterior=bNovo[i]
    return wNovo,bNovo
```

Por fim há a função de ativação e validação do neuronio, que a partir da equação abaixo,
obtemos o resultado do neuronio treinado e recebemos a comparação entre o resultado esperado e obtido

<img src=https://latex.codecogs.com/gif.latex?y%3D%5Csum_j%20w_jx_j>

```
python
def ativacao_validacao(t,s,w,b):
    limiar = 0 
    for i in range(16):
        print("Caso ["+str(i)+"]")
        for j in range(4):
            yLiquido = (w[i][0]*s[j][0])+(w[i][1]*s[j][1])+b[i]
            if(yLiquido>=limiar):
                y=1
            else:
                y=-1
            if(y==t[i][j]):
                flag=" [Pass]"
            else:
                flag=" [Fail]"
            print(" Expectativa: " + str(int(t[i][j])) + " Resultado: " + str(y) + flag)
        print("Pesos: "+ str(w[i]) + " Bias: "+ str(b[i])+"\n")

    return 0
```

# Resltado Final

```
Caso [0]
 Expectativa: 0 Resultado: 1 [Fail]
 Expectativa: 0 Resultado: 1 [Fail]
 Expectativa: 0 Resultado: 1 [Fail]
 Expectativa: 0 Resultado: 1 [Fail]
Pesos: [0. 0.] Bias: 0.0

Caso [1]
 Expectativa: 0 Resultado: -1 [Fail]
 Expectativa: 0 Resultado: 1 [Fail]
 Expectativa: 0 Resultado: 1 [Fail]
 Expectativa: 1 Resultado: 1 [Pass]
Pesos: [1. 1.] Bias: 1.0

Caso [2]
 Expectativa: 0 Resultado: 1 [Fail]
 Expectativa: 0 Resultado: -1 [Fail]
 Expectativa: 1 Resultado: 1 [Pass]
 Expectativa: 0 Resultado: 1 [Fail]
Pesos: [ 1. -1.] Bias: 1.0

Caso [3]
 Expectativa: 0 Resultado: 1 [Fail]
 Expectativa: 0 Resultado: 1 [Fail]
 Expectativa: 1 Resultado: 1 [Pass]
 Expectativa: 1 Resultado: 1 [Pass]
Pesos: [2. 0.] Bias: 2.0

Caso [4]
 Expectativa: 0 Resultado: 1 [Fail]
 Expectativa: 1 Resultado: 1 [Pass]
 Expectativa: 0 Resultado: -1 [Fail]
 Expectativa: 0 Resultado: 1 [Fail]
Pesos: [-1.  1.] Bias: 1.0

Caso [5]
 Expectativa: 0 Resultado: 1 [Fail]
 Expectativa: 1 Resultado: 1 [Pass]
 Expectativa: 0 Resultado: 1 [Fail]
 Expectativa: 1 Resultado: 1 [Pass]
Pesos: [0. 2.] Bias: 2.0

Caso [6]
 Expectativa: 0 Resultado: 1 [Fail]
 Expectativa: 1 Resultado: 1 [Pass]
 Expectativa: 1 Resultado: 1 [Pass]
 Expectativa: 0 Resultado: 1 [Fail]
Pesos: [0. 0.] Bias: 2.0

Caso [7]
 Expectativa: 0 Resultado: 1 [Fail]
 Expectativa: 1 Resultado: 1 [Pass]
 Expectativa: 1 Resultado: 1 [Pass]
 Expectativa: 1 Resultado: 1 [Pass]
Pesos: [1. 1.] Bias: 3.0

Caso [8]
 Expectativa: 1 Resultado: 1 [Pass]
 Expectativa: 0 Resultado: 1 [Fail]
 Expectativa: 0 Resultado: 1 [Fail]
 Expectativa: 0 Resultado: -1 [Fail]
Pesos: [-1. -1.] Bias: 1.0

Caso [9]
 Expectativa: 1 Resultado: 1 [Pass]
 Expectativa: 0 Resultado: 1 [Fail]
 Expectativa: 0 Resultado: 1 [Fail]
 Expectativa: 1 Resultado: 1 [Pass]
Pesos: [0. 0.] Bias: 2.0

Caso [10]
 Expectativa: 1 Resultado: 1 [Pass]
 Expectativa: 0 Resultado: 1 [Fail]
 Expectativa: 1 Resultado: 1 [Pass]
 Expectativa: 0 Resultado: 1 [Fail]
Pesos: [ 0. -2.] Bias: 2.0

Caso [11]
 Expectativa: 1 Resultado: 1 [Pass]
 Expectativa: 0 Resultado: 1 [Fail]
 Expectativa: 1 Resultado: 1 [Pass]
 Expectativa: 1 Resultado: 1 [Pass]
Pesos: [ 1. -1.] Bias: 3.0

Caso [12]
 Expectativa: 1 Resultado: 1 [Pass]
 Expectativa: 1 Resultado: 1 [Pass]
 Expectativa: 0 Resultado: 1 [Fail]
 Expectativa: 0 Resultado: 1 [Fail]
Pesos: [-2.  0.] Bias: 2.0

Caso [13]
 Expectativa: 1 Resultado: 1 [Pass]
 Expectativa: 1 Resultado: 1 [Pass]
 Expectativa: 0 Resultado: 1 [Fail]
 Expectativa: 1 Resultado: 1 [Pass]
Pesos: [-1.  1.] Bias: 3.0

Caso [14]
 Expectativa: 1 Resultado: 1 [Pass]
 Expectativa: 1 Resultado: 1 [Pass]
 Expectativa: 1 Resultado: 1 [Pass]
 Expectativa: 0 Resultado: 1 [Fail]
Pesos: [-1. -1.] Bias: 3.0

Caso [15]
 Expectativa: 1 Resultado: 1 [Pass]
 Expectativa: 1 Resultado: 1 [Pass]
 Expectativa: 1 Resultado: 1 [Pass]
 Expectativa: 1 Resultado: 1 [Pass]
Pesos: [0. 0.] Bias: 4.0
```

# Conclusão

Pode-se concluir que obtivemos sucesso em alcançar o objetivo do experimento. Encontramos os pesos de 14 das 16 funções lógicas e chegamos ao resultado esperado pelas tabelas
verdades originais.
As duas funções a qual não encontramos os correspondentes foram de Ou Exclusivo e de
Bicondicional
