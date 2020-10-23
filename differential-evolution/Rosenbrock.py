#variacao
import numpy as np
import numpy.matlib
import random
li = np.array([-1, -1])
ls = np.array([2, 2])

def rosenbrock(x):
    f = (1-x[0])*(1-x[0]) + 100*(x[1]-x[0]*x[0])*(x[1]-x[0]*x[0])
    return f

def mutation(F,x1,x2,x3):
    mut=x1+F*(x2-x3)
    return mut
Gen=150
TamPop=100
PC=0.9
F=0.5

#Estrutura de dados
aptidao_pop = np.zeros(TamPop)

aptidao_trial = np.zeros(TamPop)

quant_var = len(li)

vet_trial = np.zeros((TamPop,quant_var))

vet_mutation = np.zeros((TamPop,quant_var))

pop = numpy.matlib.repmat(li,TamPop,1)+numpy.matlib.repmat((ls-li),TamPop,1)*np.random.rand(TamPop,quant_var)

gen_atual=1
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
melhorindividuo=pop[0]
for individuo in pop:
    if(rosenbrock(individuo)<=rosenbrock(melhorindividuo)):
        melhorindividuo=individuo
    else:
        pass

print(melhorindividuo)



    
