#include<stdio.h>

int main()
{
    char letra;
    int numl;

    scanf("%s", &letra);

    printf("%c\n", letra);
    
    numl = letra;

    printf("%d\n", numl);

    numl = numl + 32;

    letra = numl;

    printf("%c\n", letra);
}