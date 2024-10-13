def removeElement(nums, val):
    k = 0
    first = 0
    second = 1
    # if array is empty return
    index = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[index] = nums[i]
            index += 1
    return index


nums = [0,1,2,2,3,0,4,2]
val = 2
ans = removeElement(nums, val)
print(ans)
# ans = [2, 2, 3, 3] or [2, 2, _, _]