import numpy as np

def treinamento_multilayer_perceptron(x,t,v,w,bv,bw,neuronios):
    alfa=float(input("\nTaxa de aprendizagem: "))
    erroMin=float(input("\nErro total admissivel: "))
    max_ciclos=int(input("\nNumero de Ciclos maximo:"))
    deltinha_v = z_in = z = delta_w = delta_bv = np.zeros(neuronios['escondidos'])
    delta_v = np.zeros((neuronios['entrada'],neuronios['escondidos']))
    deltinha_w=0
    ciclo=0
    erroQ=10
    while ciclo<max_ciclos and erroQ>erroMin:
        erroQ=0
        ciclo=ciclo+1
        for i in range(4):
            for j in range(neuronios['escondidos']):
                z_in[j]=x[i][0]*v[0][j] + x[i][1]*v[1][j] + bv[j]
                z[j]= (2/(1+np.exp(-z_in[j])))-1
            y_in=np.sum(z*w)+bw
            y=(2/(1+np.exp(-y_in)))-1
    
        ############ FASE DE RETROPROPAGAÇÃO

        deltinha_w = (t[i] - y)*0.5*(1+y)*(1-y)

        for j in range(neuronios['escondidos']):
            delta_w[j]=alfa*deltinha_w*z[j]

        delta_bw=alfa*deltinha_w

        for j in range(neuronios['escondidos']):
            deltinha_v[j]=deltinha_w*w[j]*0.5*(1+z[j])*(1-z[j])

        for j in range(neuronios['entrada']):
            for k in range(neuronios['escondidos']):
                delta_v[j][k]=alfa*deltinha_v[k][0]*x[i][j]

        for j in range(neuronios['escondidos']):
            delta_bv[j] = alfa * deltinha_v[j][0]

        w=w+delta_w
        bw=bw+delta_bw

        for j in range(neuronios['entrada']):
            for k in range(neuronios['escondidos']):
                v[j][k]=v[j][k]+delta_v[j][k]

        for j in range(neuronios['escondidos']):
            bv[j] = bv[j]+delta_bv[j]

        erroQ = erroQ + 0.5*((t[i]-y)*(t[i]-y))
        print("\nCiclo "+ str(ciclo) + ": "+ str(erroQ))    
    print("Fim do Treinamento\n"+
      "Erro Quadrático final: " + str(erroQ) + "\n" +
      "Ciclos: " + str(ciclo) +"\n" +
      "\n\n")

    return v,w,bv,bw

def validacao(x,t,v,w,bv,bw,hl):
    z = z_in=np.zeros(hl)
    print("\n\n TESTE DO TREINAMENTO\n\n")
    for i in range(4):
        for j in range(neuronios['escondidos']):
            z_in[j]=x[i][0]*v[0][j] + x[i][1]*v[1][j] + bv[j]
            z[j]= (2/(1+np.exp(-z_in[j])))-1
        y_in=np.sum(z*w)+bw
        y=(2/(1+np.exp(-y_in)))-1
        print("Target: " + str(t[i]) +"   Rede Treinada: " + str(y))
            

#entradas e saidas

source = [[1.0,1.0],
          [1.0,-1.0],
          [-1.0,1.0],
          [-1.0,-1.0]]

target = [-1.0,
           1.0,
           1.0,
          -1.0]

#define a arquitetura do neuronio
neuronios = {'escondidos': int(input("Digite o numero de camadas escondidas: ")),'saida': 1,'entrada': 2}



#Inicializa pesos
#pesos e bias camada escondida
hidden_weights  = np.random.rand(neuronios['entrada'],neuronios['escondidos'])-0.5
hidden_bias = np.random.rand(neuronios['escondidos'],1)-0.5

#pesos e bias camada de saida
output_weights = np.random.rand(neuronios['escondidos'],neuronios['saida'])-0.5
print(output_weights)
output_bias = np.random.rand()-0.5

hidden_weights,output_weights,hidden_bias,output_bias = treinamento_multilayer_perceptron(source,target,hidden_weights,output_weights,hidden_bias,output_bias,neuronios)
validacao(source,target,hidden_weights,output_weights,hidden_bias,output_bias,neuronios['escondidos'])
