from libs.linhas import *
a=input("digite um ano: ")
e=input("digite um estado: ")

total=0
f=open("incendiodata.csv", "r")
if f:
    for linha in f:
        n=countparts(linha, ",")
        p1=getpart(linha, ",",1)
        p2=getpart(linha, ",", 2)
        p=getpart(linha, ",", 4)
        print(p1)
        print(p2)
    print(n)
    
    """p4=int(p)"""


    if p1 == a and p2 == e:
            print ("ok")
    else:
            print("not ok")
            """total += p4
    print("o total de incêndios em {} em {} foi de {}".format(a, e, total))
    f.close
else:
    print("não foi possível ler o arquivo")""Santa Catarina"""