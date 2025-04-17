
def merge(start: int, mid: int, end: int):
    tmp_arr = []
    i,j = start, mid+1
    while (i<=mid and j<=end):
        if arr[i] <= arr[j]:
            tmp_arr.append(arr[i])
            i += 1
        else:
            tmp_arr.append(arr[j])
            j +=1
    
    while i<=mid:
        tmp_arr.append(arr[i])
        i +=1
    
    while j<=end:
        tmp_arr.append(arr[j])
        j += 1
    arr[start:end+1] = tmp_arr



def merge_sort(start: int, end: int):
    if start < end:
        mid = (start + end)//2
        merge_sort(start, mid)
        merge_sort(mid+1, end)
        merge(start, mid, end)
    

arr = [1,2,8,5,3,-1]
merge_sort(0, len(arr)-1)
print(arr)