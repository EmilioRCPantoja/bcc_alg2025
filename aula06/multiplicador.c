#include<stdio.h>
#include"libs/fat.h"

int main()
{
    int a;
    printf("digite um numero: ");
    scanf("%d", &a);
    a= fat(a);
    printf("%d", a);
return 0;
}