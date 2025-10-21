def longestConsecutive(nums):
    numbers_visted = set(nums)

    if nums_length == 0:
        return 0

    if nums_length == 1:
        return 1



    for i in nums:
        if i not in unique_numbers_map:
            unique_numbers_map[i] = 1

    longest_consec_len = 1
    for i in unique_numbers_map:
        if i not in numbers_visted:
            numbers_visted.add(i)
            if i+1 in unique_numbers_map and i+1 not in numbers_visted:
                numbers_visted.add(i+1)
                longest_consec_len += 1

            if i-1 in unique_numbers_map and i-1 not in numbers_visted:
                numbers_visted.add(i-1)
                longest_consec_len += 1

    return longest_consec_len+1



print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
