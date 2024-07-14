# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def mergeTwoLists(list1, list2):
    finallis = []
    if list1 == None:
        return list2
    elif list2 == None:
        return list2
    elif list1 and list2 == None:
        return []

    l1 = list1[0]
    l2 = list2[0]

    while l1 != None and l2 != None:
        if l1 != None and l2  == None:
            finallis.append(l1.val)
        elif l1 == None and l2 != None:
            finallis.append(l2.val)
        else:
            if l1.val > l2.val:
                finallis.append(l2.val)
                l2 = l2.next
            elif l1.val < l2.val:
                finallis.append(l1.val)
            elif l1 == l2:
                finallis.append(l1.val)
                finallis.append(l2.val)
                l1 = l1.next
                l2 = l2.next

    return finallis




list1 = [1,2,4]
list2 = [1,3,4]

print(mergeTwoLists(list1, list2))