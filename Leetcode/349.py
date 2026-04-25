# def intersection(nums1, nums2):
#     ans_array = []
#     if len(nums1) < len(nums2):
#         map_array = nums1
#         other_array = nums2
#     else:
#         map_array = nums2
#         other_array = nums1
#     hash_map = {}
#     for i in range(len(map_array)):
#         if map_array[i] not in hash_map:
#             hash_map[map_array[i]] = 1
#
#     for i in range(len(other_array)):
#         if other_array[i] in hash_map:
#             ans_array.append(other_array[i])
#             del hash_map[other_array[i]]
#     return ans_array


def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersection(nums1, nums2))
