larg = int(input("digite a largura do triangulo: "))
i=0
print("#")
while i <=(larg-2)/2:
    print("#"+"-"*i*2+"#")
    i+=1
while i > 0:
    if i == (larg-2)/2:
        i=i-2
    else:
        print("#"+"-"*i*2+"#")
        i=i-1

print("#")