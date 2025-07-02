
def bubble_sort(arr):
    aux=0
    troca = 0
    for n in range(len(arr)- 1,0,-1):
        troca=0
        for i in range(n):
            if arr[i] > arr[i+1]:
                aux=arr[i]
                arr[i]=arr[i+1]
                arr[i+1]=aux
                troca=1
        if troca==0:
            break



f = open("numeros.txt", "r")
numeros = []

if f:
    for linha in f:
         numeros.append(linha)
    