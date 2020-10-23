import numpy as np

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

#Inicializacao dos targets das tabelas verdades
target=generate_tables()

#Inputs
source = [[-1,-1],
        [-1,1],
        [1,-1],
        [1,1]]

#Treinamento e obtencao dos pesos e bias
weights,bias = treinamento_hebb(target,source)

#Ativacao e validacao dos pesos obtidos
ativacao_validacao(target,source,weights,bias)