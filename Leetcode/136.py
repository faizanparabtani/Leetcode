def singleNumber(nums):
    xor = 0
    for num in nums:
        xor ^= num

    return xor