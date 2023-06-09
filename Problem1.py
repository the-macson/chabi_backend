# Algorithm: Selection Sort

def selection_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1,len(arr)):
            if arr[min]>arr[j]:
                min = j
        arr[i],arr[min] = arr[min],arr[i]
    return arr

print(selection_sort([5,416,54,21,6135,15,741]))