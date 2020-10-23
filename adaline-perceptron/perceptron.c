#include <stdio.h>
#include <stdlib.h>

int main(){
    float yLiquido, y, trocou=1,ciclos;
    float wAnterior[2] = {0,0};
    float bAnterior, teta = 0;
    float wNovo[2]={0,0};
    float bNovo=0;
    float alfa = 1;

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

        while(trocou == 1){
            trocou=0;
            ciclos=ciclos+1;
            printf("Ciclo %.0f => ",ciclos);
            printf("wnovo[0]:%.1f wnovo[1]: %.1f   bnovo: %.1f  \n",wNovo[0],wNovo[1],bNovo);
                for (int i=0;i<14;i++){
                yLiquido = wAnterior[0] * s[i][0] + wAnterior[1] * s[i][1] + bAnterior;
                
                if(yLiquido>= teta){
                    y=1;
                    }

                else{   
                    y=-1;
                    }

                if(y!=t[i]){
                    trocou=1;
                    for(int z=0;z<2;z++){
                        wNovo[z]=wAnterior[z]+ alfa*s[i][z]*t[i];
                        wAnterior[z]=wNovo[z];
                        }  
                    bNovo=bAnterior+ alfa*t[i];
                    bAnterior=bNovo;
                }   
                }    
        printf("\n\n");
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
