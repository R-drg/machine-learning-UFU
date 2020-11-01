# Differential Evolution

## Introdução

Na computação evolutiva, a evolução diferencial é um método que otimiza um problema tentando iterativamente 
melhorar uma solução candidata em relação a uma determinada medida de qualidade

## Objetivos

+ Minimizar a função de Rosenbrock

<img src="https://latex.codecogs.com/gif.latex?f%28x%29%20%3D%20%5Csum_%7Bi%3D1%7D%5E%7BD-1%7D%281-x_i%29%5E2&plus;100%28x_%7Bi&plus;1%7D-x_i%5E2%29%5E2" />

## Desenvolvimento

Utilizando o codigo em python (Rosenbrock.py), foi realizado a Evolução Diferencial a fim de
minimizar a função de Rosenbrock

Função de Rosenbrock

```python
def rosenbrock(x):
    f = (1-x[0])*(1-x[0]) + 100*(x[1]-x[0]*x[0])*(x[1]-x[0]*x[0])
    return f
```

Função que realiza a mutação atráves da seleção de 3 pontos randômicos
```python
def mutation(F,x1,x2,x3):
    mut=x1+F*(x2-x3)
    return mut
```

Realiza o treinamento através da evolução de gerações
```python
while(gen_atual<=Gen):
    print("Geração ["+str(gen_atual)+"]")
    gen_atual=gen_atual+1
    for p in range(TamPop):
        x1=pop[random.randint(0,TamPop-1)]
        x2=pop[random.randint(0,TamPop-1)]
        x3=pop[random.randint(0,TamPop-1)]
        vet_mutation[p] = mutation(F,x1,x2,x3)
    for p in range(TamPop):
        if(random.uniform(0, 1)<=PC):
            vet_trial[p]=vet_mutation[p]
        else:
            vet_trial[p]=pop[p]
    for p in range(TamPop):
        if(rosenbrock(vet_trial[p])<rosenbrock(pop[p])):
            pop[p]=vet_trial[p]
        else:
            pop[p]=pop[p]
```

Encontra o melhor indivíduo
```python
melhorindividuo=pop[0]
for individuo in pop:
    if(rosenbrock(individuo)<=rosenbrock(melhorindividuo)):
        melhorindividuo=individuo
    else:
        pass
```

## Resultado
Após a Evolução e um total de 150 gerações, obtivemos o melhor indivíduo [1. 1.]
Ao passar ele pela função rosenbrock, obtivemos 0, que é o menor valor possível
