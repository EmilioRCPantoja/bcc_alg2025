import random
vetor=[]
aux=0
t=0
for i in range(20):
    n = i
    vetor.append(n)

for j in range(len(vetor)-1):
    for t in range(j):
        if vetor[t]%2 == 0:
            aux = vetor[t]
            vetor[t] = vetor[t+1]
            vetor[t+1] = aux
print(vetor)
