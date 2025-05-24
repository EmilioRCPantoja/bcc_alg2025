#iniciar
i=0
#criar sinalizador de troca
troca=1
#criar vetor
vetor =[]
#criar auxiliar de troca
aux=0
# fazer a função de ordenação
def bubble_sort(arr):
    #percorrer o vetor inteiro
    for n in range(len(vetor)- 1,0,-1):
        #supor que não houve troca
        troca=0
        #enquanto percorrer o vetor
        for i in range(n):
            #se o número atual for maior que o próximo
            if vetor[i] > vetor[i+1]:
                #trocar os dois de lugar
                aux=vetor[i]
                vetor[i]=vetor[i+1]
                vetor[i+1]=aux
                #sinalizar que houve troca
                troca=1
        #se não houver troca
        if troca==0:
            #parar de percorrer o vetor
            break
#criar laço de 10 repetições
for i in range(10):
    #pedir um número inteiro positivo
    num = int(input("digite um número inteiro positivo: "))
    #armazenar ele e "vetor"
    vetor.append(num)
    #se o número for 0
    if num == 0:
        #parar de pedir número
        break
#ordenar o vetor
bubble_sort(vetor)
#somar os dois maiores números
soma = vetor[len(vetor) - 1] + vetor[len(vetor) - 2]
#mostrar a soma deles
print(soma)
