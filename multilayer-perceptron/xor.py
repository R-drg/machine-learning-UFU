import math,random,numpy

dots=open('dots.txt','a')
cicles=open('cicles.txt','a')

deltinhainv = []
deltinhav = []
z = []
zin = []
deltaw = []
deltav = []
deltabv = []

x= [[1.0,1.0],
    [1.0,-1.0],
    [-1.0,1.0],
    [-1.0,-1.0]]

t = [-1.0,
     1.0,
     1.0,
     -1.0]
yin=0
neuroniosentrada = 2
neuroniosescondidos=int(input("Numero de neuronios escondidos: "))
neuroniossaida = 1
alfa=float(input("\nTaxa de aprendizagem: "))
erroMin=float(input("\nErro total admissivel: "))
numCiclo=int(input("\nNumero de Ciclos maximo:"))

for j in range(neuroniosentrada):
    lista=[]
    for k in range(neuroniosescondidos):
        lista.append(0)
    deltav.append(lista)

#inicialização pesos da camada escondida
v=numpy.random.rand(neuroniosentrada,neuroniosescondidos)-0.5
bv = numpy.random.rand(neuroniosescondidos,1)-0.5
for i in range(neuroniosescondidos):
    deltinhainv.append(0)
    deltinhav.append(0)
    zin.append(0)
    z.append(0)
    deltaw.append(0)
    deltabv.append(0)

#Inicialização pesos de saida
deltinhaw=0
w=numpy.random.rand(neuroniosescondidos,neuroniossaida)-0.5
bw=numpy.random.rand()-0.5

ciclo=0
erroQ=10
while ciclo<numCiclo and erroQ>erroMin:
    erroQ = 0
    ciclo=ciclo+1
    for i in range(4):
        for j in range(neuroniosescondidos):
            zin[j]=x[i][0]*v[0][j] + x[i][1]*v[1][j] + bv[j]
            z[j]= (2/(1+math.exp(-zin[j])))-1
        yin=numpy.sum(z*w)+bw
        y=(2/(1+math.exp(-yin)))-1

############ FASE DE RETROPROPAGAÇÃO

        deltinhaw = (t[i] - y)*0.5*(1+y)*(1-y)

        for j in range(neuroniosescondidos):
            deltaw[j]=alfa*deltinhaw*z[j]

        deltabw=alfa*deltinhaw

        for j in range(neuroniosescondidos):
            deltinhav[j]=deltinhaw*w[j]*0.5*(1+z[j])*(1-z[j])

        for j in range(neuroniosentrada):
            for k in range(neuroniosescondidos):
                deltav[j][k]=alfa*deltinhav[k][0]*x[i][j]

        for j in range(neuroniosescondidos):
            deltabv[j] = alfa * deltinhav[j][0]

        w=w+deltaw
        bw=bw+deltabw

        for j in range(neuroniosentrada):
            for k in range(neuroniosescondidos):
                v[j][k]=v[j][k]+deltav[j][k]

        for j in range(neuroniosescondidos):
            bv[j] = bv[j]+deltabv[j]
        
    erroQ = erroQ + 0.5*((t[i]-y)*(t[i]-y))
    dots.write(str(erroQ)+"\n")
    cicles.write(str(ciclo)+"\n")
    print("\nCiclo "+ str(ciclo) + ": "+ str(erroQ))
cicles.close()
dots.close()
print("Fim do Treinamento\n"+
      "Erro Quadrático final: " + str(erroQ) + "\n" +
      "Ciclos: " + str(ciclo) +"\n" +
      "Pesos encontrados:" + str(w) + "\n"
      "\n\n")
print("\n\n TESTE DO TREINAMENTO\n\n")
for i in range(4):
    for i in range(4):
        for j in range(neuroniosescondidos):
            zin[j]=x[i][0]*v[0][j] + x[i][1]*v[1][j] + bv[j]
            z[j]= (2/(1+math.exp(-zin[j])))-1
        yin=numpy.sum(z*w)+bw
        y=(2/(1+math.exp(-yin)))-1
        print("Target: " + str(t[i]) +"   Rede Treinada: " + str(y))
        