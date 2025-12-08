def mergeTwoLists(list1, list2):
    # Check if any list is empty
    dummy = ListNode()
    tail = dummy

    # Traverse both lists and pick the smaller value each time
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    # Attach remaining nodes (only one of these can be non-null)
    if list1:
        tail.next = list1
    else:
        tail.next = list2

    return dummy.next