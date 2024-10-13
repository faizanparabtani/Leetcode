def containsDuplicate(nums):
    visited = {}
    for i in nums:
        print(i, visited)
        if i in visited:
            return "true"
        else:
            visited[i] = 1
        
    return "false"


print(containsDuplicate([1, 2, 3, 4]))