# My attempt
# def summaryRanges(nums):
#     slow = 0
#     fast = 1
#     numslen = len(nums)
#     ans_array = []
#
#     if numslen == 0:
#         return []
#     elif numslen == 1:
#         return [str(nums[0])]
#
#     while fast < numslen:
#         if nums[fast - 1] + 1 != nums[fast]:
#             if nums[slow] == nums[fast - 1]:
#                 ans_array.append(f"{nums[slow]}")
#                 slow = fast
#             else:
#                 formatted_range = f"{nums[slow]} -> {nums[fast - 1]}"
#                 ans_array.append(formatted_range)
#                 slow = fast
#         fast += 1
#
#     if slow != fast and fast == len(nums):
#         ans_array.append(f"{nums[slow]}->{nums[fast - 1]}")
#     return ans_array


def summaryRanges(nums):
    if not nums:
        return []

    result = []
    i = 0
    while i < len(nums):
        start = nums[i]
        j = i
        # Expand the range as long as elements are consecutive
        while j + 1 < len(nums) and nums[j + 1] == nums[j] + 1:
            j += 1

        # Format the range string
        if nums[j] == start:
            result.append(str(start))
        else:
            result.append(f"{start}->{nums[j]}")

        # Move to the next potential start of a range
        i = j + 1
    return result


nums = [0, 7, 8, 10]
result = summaryRanges(nums)
print(result)

