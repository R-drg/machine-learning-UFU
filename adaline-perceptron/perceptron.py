import numpy as np
import random

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
                    trocou=1
                    for z in range(2):
                        wNovo[z]=wAnterior[z]+ alfa*s[i][z]*t[i]
                        wAnterior[z]=wNovo[z]
                    bNovo=bAnterior+ alfa*t[i]
                    bAnterior=bNovo
        ciclo+=1
        print("wnovo[0]:%.4f  wnovo[1]: %.4f  bnovo: %.4f" % (wNovo[0],wNovo[1],bNovo))
    return wNovo,bNovo

def ativacao(w,b,t,s):
    teta = 0
    print("\n\nResultados:\n")
    print("Pesos finais: "+str(w) +" Bias final: "+ str(b))
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
weights,bias=treinamento_perceptron(maxCiclos,alfa,target,source)
#ativacao
ativacao(weights,bias,target,source)
