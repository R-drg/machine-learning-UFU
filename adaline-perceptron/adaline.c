#include <stdio.h>
#include <stdlib.h>
#include <time.h>


double getfrand(double fmin, double fmax)
{
   static int Init=0;
   double rc;
   if (Init==0)
   {
      srand(time(NULL));
      Init=1;
   }
   rc= ((double)rand()/RAND_MAX) * (fmax - fmin) + fmin;
   return (rc);
};


int main(){
    float yLiquido, y, trocou=1;
    float teta = 0;
    float erroQ = 0;
    float wNovo[2]={0,0};
    float bNovo=0;
    float alfa = 0.1;
    int maxCiclos = 300;
    int ciclos = 0;

//Inicializando pesos
    float wAnterior[2] = {getfrand(-0.5,0.5),getfrand(-0.5,0.5)};
    float bAnterior = getfrand(-0.5,0.5);


//Define os valores de T

    float t[14] = {1,1,-1,1,1,-1,1,-1,-1,1,-1,-1,1,-1};

//Define os valores de S

    float s[14][2] = {{1.0,1.0},
                    {1.1,1.5},
                    {2.5,1.7},
                    {1.0,2.0},
                    {0.3,1.4},
                    {2.8,1.0},
                    {0.8,1.5},
                    {2.5,0.5},
                    {2.3,1.0},
                    {0.5,1.1},
                    {1.9,1.3},
                    {2.0,0.9},
                    {0.5,1.8},
                    {2.1,0.6}};

    while(ciclos<=maxCiclos){
        erroQ=0;
        printf("Ciclo %i => ",ciclos);
        for(int i=0;i<14;i++){
            yLiquido = wAnterior[0]*s[i][0] + wAnterior[1]*s[i][1] + bAnterior;
            erroQ = erroQ + (t[i]-yLiquido)*(t[i]-yLiquido);
            wNovo[0]= wAnterior[0] + alfa*(t[i]-yLiquido)*s[i][0];
            wAnterior[0] = wNovo[0];
            wNovo[1]= wAnterior[1] + alfa*(t[i]-yLiquido)*s[i][1];
            wAnterior[1] = wNovo[1];
            bNovo = bAnterior + alfa*(t[i]-yLiquido);
            bAnterior = bNovo;
        }
        printf("wnovo[0]:%.1f wnovo[1]: %.1f   bnovo: %.1f     erroQ:%.1f\n",wNovo[0],wNovo[1],bNovo,erroQ);
        ciclos++;
    }



        printf("Resultados:\n");

        printf("\n\nExpectativa:     Resultado:\n");
        for(int j=0;j<14;j++){
            yLiquido = (wNovo[0]*s[j][0])+(wNovo[1]*s[j][1])+bNovo;
            if(yLiquido>= teta){
                y=1;
            }
            else{
                y=-1;
            }
            printf("%.1f %.1f %.1f            %.1f %.1f %.1f",s[j][0],s[j][1],t[j],s[j][0],s[j][1],y);
            if(t[j] == y){
                printf("  [Pass]\n");
            }
            else{
                printf("    [Fail]\n");
            }
        }

};
