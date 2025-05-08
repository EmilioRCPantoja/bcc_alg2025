#criar e ler a variavel comprimentoterreno 
compterreno = int(input("digite o comprimento do terreno: "))
#criar e ler a variavel larguracomprimento
largterreno = int(input("digite a largura do terreno: "))

# criar a variavel areaterreno
# multiplicar larguraterreno pelo comprimentoterreno e armazenar na variavel areaterreno
areaterreno = largterreno * compterreno

# criar e ler a variavel comprimentocasa
compcasa = int(input("digite o comprimento da casa: "))

# criar e ler a variavel larguracasa
largcasa = int(input("digite a largura da casa: "))

# criar a variavel areacasa
# multiplicar comprimentocas por larguracasa e armazenar em areacasa
areacasa = compcasa * largcasa

# criar a variavel arealivre
# subtrair areacasa de areaterreno e armazenar o resultado em arealivre
arealivre = areaterreno - areacasa

# mostrar arealivre
print("a área livre será de {} m²".format(arealivre)) 