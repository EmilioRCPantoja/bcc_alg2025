i=1
vetor=[]


def bubble_sort(vetor):
    troca=1
    aux=0
    for n in range(len(vetor)- 1,0,-1):
        troca=0
        for i in range(n):
            if vetor[i] > vetor[i+1]:
                aux=vetor[i]
                vetor[i]=vetor[i+1]
                vetor[i+1]=aux
                troca=1
        if troca==0:
            break

for i in range(10):
    num= int(input("digite um número: "))
    vetor.append(num)

bubble_sort(vetor)
print("a ordem será: \n")
for i in range(10):
    print(vetor[i])