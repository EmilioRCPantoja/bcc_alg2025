#criar e ler a variavel minutostotais
minutostotais = (float(input("digite a quantidade de minutos: ")))

#criar a variavel horas
#criar a variavel minutos
#criar a variavel segundos

#dividir minutostotais po 60 e armazenar a parte inteira em 'horas'
horas = int(minutostotais/60)

#diminuir minutostotais pelo produto de 'horas' * 60, e armazenar a parte inteira desse resultado em 'minutos'
minutos = minutostotais - (horas*60)

#se 'minutostotais' tiver parte decimal
if minutostotais > int(minutostotais):
    
    #multiplicar essa parte decimal por 60 e armazenar em 'segundos'
    segundos = (minutostotais - int(minutostotais))*60
else:
    segundos=0
#mostrar horas, minutos e segundos sem quebra de linha
print("{} horas, {} minutos, {} segundos".format(horas, minutos, segundos))
