from typing import List


data  = [9, 5, 1, 3, 4, 7, 8,2]

# Compara os pares adjacentes
def bubblesort(v: List[int]) -> List[int]:
    for i in range(0,len(v)):
        for j in range(0,len(v)-1):
            if v[j] > v[j+1]:
                v[j], v[j+1] = v[j+1], v[j]
    return v

print(bubblesort(data))

