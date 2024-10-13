from collections import Counter


# def majorityElement(nums):
#     nums_counter = Counter(nums)
#     limit = len(nums)//2
#     for i in nums_counter:
#         if nums_counter[i] > limit:
#             return i
        
# Without using counter
def majorityElement(nums):
    nums_counter = {}
    limit = len(nums)//2
    if limit == 0:
        return nums[0]
    for i in nums:
        if i in nums_counter:
            nums_counter[i] += 1
            if nums_counter[i] > limit:
                return i
        else:
            nums_counter[i] = 1




nums = [1]
print(majorityElement(nums))