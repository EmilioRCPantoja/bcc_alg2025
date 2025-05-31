quant = int(input("digite uma quantidade de números: "))
a=0
x = 0
for i in range(quant):
    n = int(input("digite um número: "))
    if a==0:
        x = x + n      
        a = 1
    
    elif a==1:
        x = x * n
        a =2

    else:
        x = x - n
        a = 0
print(x)