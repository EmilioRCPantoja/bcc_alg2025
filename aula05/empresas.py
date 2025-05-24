from biblioteca.linha import *
f = open("empresasdata.csv", "r")
aux=0
auxstr=0
troca=1
dates=[]
if f:
    for linhas in f:
        n = countparts(linhas, ",")
        date =getpart(linhas, ",", 4)
        print(date)
        if date != "year founded":
            g= countparts(linhas, ".")
            date = (getpart(date, ".", 1))
            dates.append(date)
            print(date)

    for j in range ( len(dates) -1, 0,-1):
        troca=0
        for i in j:
            if dates[i] > dates [i+1]:
                troca=1
                aux = dates[i]
                dates[i] = dates[i+1]
                dates[i+1] = aux
                auxstr = linhas[i]
                linhas[i] = linhas[i+1]
                linhas[i+1] = auxstr
        if troca == 0:
            break

    print(linhas)

    f.close
else:
    print("erro ao ler o arquivo")
