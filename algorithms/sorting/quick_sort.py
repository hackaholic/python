
def pivot(start: int, end: int) -> int:
    p_val = arr[end]

    i,j = start, start
    print(i,j, end)
    while j<=end:
        if arr[j] <= p_val:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
        j += 1
    
    arr[j], arr[i] = arr[i], arr[j]
    return i


def quick_sort(start: int, end: int):
    if start < end:
        p = pivot(start, end)
        quick_sort(start, p-1)
        quick_sort(p+1, end)

arr = [1,2,8,5,3,-1]
quick_sort(0, len(arr)-1)
print(arr)