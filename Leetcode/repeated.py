def checkRepeats(nums):
    myHashMap = {}

    for i in nums:
        if i in myHashMap:
            return True
        else:
            myHashMap[i] = i
        
    return False


nums = [1,2,3,1]

print(checkRepeats(nums))