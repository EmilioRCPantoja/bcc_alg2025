compd = int(input("digite o comprimento do deposito: "))
compcx=0
compt = [2]

caixas = 0

while compcx < compd:
    caixas += 1 

    for i in range (len(compt)):
      
        n = int(compt[i] + 1)
        compt.append(int(n))
        
        compcx = sum(compt)
        print (compt)
        
        if compcx>compd:
            break
        


print("em um corredor de comprimento {}, cabem {} caixas".format(compd, caixas))