'''

3) Faça um algoritmo que receba uma lista ordenada de números e faça uma busca binária por um
determinado número, que deve existir na lista. Forneça esse algoritmo em duas versões: a)
procedural e b) recursiva.'''



# Definir função com parametros: lista e alvo
def binarySearch(lista, target):
    # Definir indice do começo e Fim da lista
    start = 0
    end = int(len(lista) - 1)
    # Enquanto lista for diferente de alvo, faça
    while start <= end:
        # Calcular pivo ((Fim da lista - 1) /2)
        pivot = (start + end) // 2
        # Verificar em qual esta o alvo e dividir a lista
        if lista[pivot] == target:
            return pivot
        elif lista[pivot] > target:
            
            end = pivot - 1
        else:
            
            start = pivot + 1
    return lista  

l=[1, 2, 3, 4, 5]
a = binarySearch( l , 2)
print(l[a])