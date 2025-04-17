def selection_sort(arr: list):
    for i in range(len(arr)):
        min_index = i
        for j in range(i, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        
        arr[min_index], arr[i] = arr[i], arr[min_index]
    
    print(arr)
selection_sort([1,2,8,5,3,-1])

