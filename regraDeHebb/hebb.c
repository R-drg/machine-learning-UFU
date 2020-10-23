#include <stdio.h>
#include <stdlib.h>

int main(){
    int t[16][4];
    int s[4][2] = {{-1,-1},{-1,1},{1,-1},{1,1}};
    int wAnterior[2] = {0,0};
    int bAnterior, limiar = 0;
    int wNovo[16][2];
    int bNovo[16];
    int y;
    int yLiquido;

//Define os valores de T

    for (int i=0;i<16;i++){
            int num = i;
        for(int j=0;j<4;j++){
            if(num%2==1){
                t[i][j] = 1;
                num=num/2;
            }
            else{
                t[i][j]= -1;
                num=num/2;
            }
        }
    }


    for (int i=0;i<16;i++){
        wAnterior[0]=0;
        wAnterior[1]=0;
        bAnterior=0;
        for(int j=0;j<4;j++){
            for(int z=0;z<2;z++){
                wNovo[i][z]=wAnterior[z]+s[j][z]*t[i][j];
                wAnterior[z]=wNovo[i][z];
            }
            bNovo[i]=bAnterior+t[i][j];
            bAnterior=bNovo[i];
        }
        // printf("b [%i]: %i \n",i,bNovo[i]);
    }

    // printf("\n\nResultados:\n");

    for(int i=0;i<16;i++){
       printf("\n\nExpectativa[%i]:     Resultado[%i]:\n",i,i);
        for(int j=0;j<4;j++){
            yLiquido = (wNovo[i][0]*s[j][0])+(wNovo[i][1]*s[j][1])+bNovo[i];
            if(yLiquido>= limiar){
                y=1;
            }
            else{
                y=-1;
            }
            printf("%i %i %i            %i %i %i",s[j][0],s[j][1],t[i][j],s[j][0],s[j][1],y);
            if(t[i][j] == y){
                printf("  [Pass]\n");
            }
            else{
                printf("    [Fail]\n");
            }
        }
    }


};
