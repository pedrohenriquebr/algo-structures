from typing import List


data = [13,2,1,3,8,5]

def insertionsort(arr: List[int]) -> List[int]:
    for i in range(1, len(arr)):
        atual = arr[i]
        j = i-1
        while arr[j] > atual and j>=0:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = atual
    return arr


print(insertionsort(data))


