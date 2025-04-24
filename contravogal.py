#pede a string e guarda em uma variável
frase = "alo mundo" #input("digite uma frase: ")

#conta as vogais
a = frase.count("a")
e = frase.count("e")
il = frase.count("i")
o = frase.count("o")
u = frase.count("u")

vogais = [a,e,il,o,u]
vogaist=[]
vogals= ["a=", "e=", "i=", "o=", "u="]


for i in range(len(vogais)):
    if vogais[i] != 0:
        vogaist.append(vogais[i])
for i in vogaist:

    vogals.insert(i, vogaist[i-1])

print(vogaist)



