#iniciar (i=0)

#criar vetor postos[30,100,...] com a distancia entre os postos

#ler "disttotal"
#ler "rendimentocarro"
#ler "tanquecarrocheio"
#"tanquecarro" recebe o valor de "tanquecarrocheio" 
#"paradasempostos" recebe 0

#multiplicar ("disttotal"/80) * 60 e armazenar na variavel "tempodeviagem"

# para i de 0 até "disttotal" faça
    #multiplicar "tanquecarro" * "rendimentocarro" e armazenar em "quantocarroanda"
    #dividir a distancia até próximo posto (postos[i]) / "rendimentocarro" e armazenar em "gasolinaagastar"

    #se "tanquecarro" for menor que "gasolinaagastar" (precisa abastecer?)
        # adicionar 10 a "tempodeviagem"
        # encher o tanque ("tanque" recebe "tanquecheio")
        # adicionar 1 em "paradasempostos" 

    # subtrair "tanque" - "gasolinaagastar" e armazenar o resultado em tanquecarro (andar até o próximo posto)
    
    

#mostrar "tempo de viagem"
#mostrar "paradasempostos"