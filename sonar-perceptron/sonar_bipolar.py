from random import random
import numpy as np
import math

teste_entrada=[]
teste_saida=[]

def percentage(part, whole):
  return 100 * float(part)/float(whole)

def read_training():
    testingset=open("testingset","r")
    for line in testingset:
        floats =[]
        res =[]
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
            teste_saida.append(-1.0)

#listas
deltinhainv = []
deltinhav = []
z = []
zin = []
deltaw = []
deltav = []
deltabv = []

training=open('./trainingset','r')
x = []
t = []

#NUM DE NEURONIOS
neuroniosentrada = 60
neuroniossaida = 1
#PEDE INFOS
neuroniosescondidos=int(input("Numero de neuronios escondidos: "))
alfa=float(input("\nTaxa de aprendizagem: "))
erroMin=float(input("\nErro total admissivel: "))
numCiclo=int(input("\nNumero de Ciclos maximo:"))

#####INICIALIZA LISTAS######
for i in range(neuroniosescondidos):
    deltinhainv.append(0)
    deltinhav.append(0)
    zin.append(0)
    z.append(0)
    deltaw.append(0)
    deltabv.append(0)

for j in range(neuroniosescondidos):
    lista=[]
    for k in range(neuroniosentrada):
        lista.append(0)
    deltav.append(lista)

#inicializa pesos saida
w=np.random.rand(neuroniosescondidos,neuroniossaida)-0.5
bw=np.random.rand(neuroniosentrada)-0.5

#inicialização pesos da camada escondida
v=np.random.rand(neuroniosescondidos,neuroniosentrada)-0.5
bv = np.random.rand(neuroniosescondidos,1)-0.5

#Input/Output

for line in training:
    floats =[]
    res =[]
    line1= line[:(len(line)-3)]
    numbers=line1.split(",")
    if (len(numbers)>1):
        for number in numbers:
            floats.append(float(number))
        if(len(floats)!=0):
            x.append(floats)
    line2= line[len(line)-2:len(line)-1]
    if(line2=='M'):
        t.append(1.0)
    elif(line2 =='R'):
        t.append(-1.0)
training.close()
erroQ=10
ciclo=0
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
read_training()
acertos=0
resultados=open("resultados.txt","w")   
for i in range(len(teste_saida)):
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
    resultados.write("Target: " + str(teste_saida[i]) +"   Rede Treinada: " + str(y))
    if ((teste_saida[i]-y)<0.1):
        resultados.write(" [PASSED]")
        acertos=acertos+1
    else:
        resultados.write(" [FAIL]")
    resultados.write("\n ")
resultados.write("TAXA DE ACERTO: " + str(acertos) +"/"+ str(len(teste_entrada)) + " (" + str(round(percentage(acertos,len(teste_entrada)))) + "%)")
resultados.close()
weights=open("pesos","w")
weights.write("Pesos camada de saida\n")
weights.write(str(w))
weights.write("\n Pesos camada escondida")
weights.write(str(v))
weights.close
print("\n\nTAXA DE ACERTO: " + str(acertos) +"/"+ str(len(teste_entrada)) + " (" + str(round(percentage(acertos,len(teste_entrada)))) + "%)") 
