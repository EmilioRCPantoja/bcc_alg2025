#include<stdio.h>

int main()
{
    int i, aux, troca, n, num;
    int vetor[10];

    i=0;
    troca=1;

    for(i=0; i<=10; i++){
        printf("digite um numero: ");
        scanf("%d", &num);
        vetor[i]=num;
    }

    while(troca==1){

        troca=0;
        
        for(i=0;i<10;i++){

            if(vetor[i]>vetor[i+1]){
                aux=vetor[i];
                vetor[i]=vetor[i+1];
                vetor[i+1]=aux;
                troca=1;
            }

        }
    }
    printf("a ordem será:\n");
    for(i=0; i<10; i++){
        printf("%i\n", vetor[i]);
    }

}