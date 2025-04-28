# SUM II Sorted array. Two pointer pattern

def sum2(arr: list, target: int) -> tuple:
    i, j = 0, len(arr) -1

    while i<j:
        cur_sum = arr[i] + arr[j]
        if cur_sum == target:
            return i,j
        elif  cur_sum < target:
            i += 1
        
        else:
            j -= 1
    

print(sum2([0,-1], -1))


# Pattern: Hash Map Lookup
#     💬 “Have I seen the number I need already?”

# 📌 Use when:
#     You want to find pairs or combinations that add/multiply/compare to a target
#     The array is not sorted
#     You care about original indices

def twoSum(nums: list[int], target: int) -> list[int]:
    seen_dict = {}
    for i,x in enumerate(nums):
        diff = target - x
        if diff in seen_dict:
            return [seen_dict[diff], i]
        else:
            seen_dict[x] = i
