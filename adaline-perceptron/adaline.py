import numpy as np
import random

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

#Dados da entrada
source=[[1.0,1.0],
        [1.1,1.5],
        [2.5,1.7],
        [1.0,2.0],
        [0.3,1.4],
        [2.8,1.0],
        [0.8,1.5],
        [2.5,0.5],
        [2.3,1.0],
        [0.5,1.1],
        [1.9,1.3],
        [2.0,0.9],
        [0.5,1.8],
        [2.1,0.6]]
#Dados da saida
target = [1,1,-1,1,1,-1,1,-1,-1,1,-1,-1,1,-1]
maxCiclos=int(input("Defina o numero de ciclos: "))
alfa=float(input("Digite uma taxa de aprendizado: "))
#treinamento
weights,bias=treinamento_adaline(maxCiclos,alfa,target,source)
#ativacao
ativacao(weights,bias,target,source)
