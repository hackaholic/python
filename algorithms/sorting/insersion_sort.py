def insersion_sort(arr: list):
    for i in range(1, len(arr)):
        j = i
        while j>0:
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                j -= 1
            else: break

    print(arr)

def insersion_sort_shift(arr: list):
    for i in range(1, len(arr)):
        j = i-1
        tmp = arr[i]
        while j>=0:
            if arr[j] > tmp:
                arr[j+1] = arr[j]
                j -=1
            else: break    
        arr[j+1] = tmp

    print(arr)

insersion_sort([1,2,8,5,3,-1])

insersion_sort_shift([1,2,8,5,3,-1])
