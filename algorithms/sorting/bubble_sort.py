def bubble_sort(arr: list) -> list:
    while True:
        swap = False
        for i in range(len(arr) -1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swap = True
        
        if not swap:
            break
       

    print(arr)      
bubble_sort([1,2,8,5,3])
