#pedir as duas fracoes no modelo  "a/b + c/d"
fracoes = input("digite uma fração no modelo a/b + c/d: ")

#separar o recebido em "a/b" e "c/d" e guardar em "fracao1" e "fracao2", respectivamente
fracaosep = fracoes.split(" ")
fracao1 = str(fracaosep[0])# --> imprime "a/b"
fracao2 = str(fracaosep[2])# --> imprime "c/d"


# separar em "a","b","c","d", transformar os valores em inteiros e armazenar nas variaveis a, b, c, d, respectivamente
numsep1 = fracao1.split("/")
numsep2 = fracao2.split("/")

a = int(numsep1[0])
b = int(numsep1[1])
c = int(numsep2[0])
d = int(numsep2[1])


# multiplicar os valores das variaveis b e d, e armazenar o resultado na variavel denominador
denominador = b * d
# somar os produtos de b e c, com o de a e d, e armazenar o resultado na variavel numerador
numerador = (b*c) + (d*a)

#mostrar "numerador/denominador"
print("a soma será igual a: {}/{}".format(numerador, denominador))  