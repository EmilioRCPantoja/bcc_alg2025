#include<stdio.h>

int main()
{
    int i;
    int numeros[10];
    float media;

    for(i=0; i<10; i++)
    {
        printf("digite um numero: ");
        scanf("%d", &numeros[i]);
        if(i>0)
        {
            media = numeros[i] + numeros[i-1];
            numeros[i]=media;
        }
    }
        
    printf("%0.2f\n", media/10);

}