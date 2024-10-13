def isPalindrome(x):
    x_str = str(x)
    left = 0
    right = len(x_str) - 1

    while left < right:
        print(x_str[left], x_str[right], ord(x_str[left]), ord('-'))
        if x_str[left] == "-":
            return "false"
        elif x_str[left] != x_str[right]:
            return "false"
        left += 1
        right -= 1

    return "true"




print(isPalindrome(-121))