
def runningSum(nums):
    sumofele = 0
    newlis = []
    for i in nums:
        sumofele += i
        newlis.append(sumofele)

    return newlis



lis = [1, 2, 3, 4]
print(runningSum(lis))