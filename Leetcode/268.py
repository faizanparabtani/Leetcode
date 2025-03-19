def missingNumber(nums):
    sum_of_nos = sum(nums)
    # actual_sum
    actual_sum = 0
    for i in range(0, len(nums)+1):
        actual_sum += i

    return actual_sum - sum_of_nos 


nums = [0,1]
print(missingNumber(nums))