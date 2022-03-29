from typing import List
data = [13,2,1,3,8,5]


# Selecionar o índice do menor elemento de uma sublista
def selectionsort(arr: List[int]) -> List[int]:
    '''
    1. Procurar menor elemento da lista
    2. Trocar de posição entre o menor elemento achado com o primeira posição
    3. Repita o 1º, incrementa a posição 
    '''

    for j in range(len(arr)-1):
        menor_idx = j
        for i in range(j, len(arr)):
            if arr[i] < arr[menor_idx]:
                menor_idx = i
        if arr[j] > arr[menor_idx]:
            arr[j], arr[menor_idx] = arr[menor_idx], arr[j]


        

    return arr



print(selectionsort(data))