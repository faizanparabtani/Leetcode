# def strStr(haystack, needle):
    # for i in range(len(haystack) - len(needle)+1):
    #     if haystack[i:i+len(needle)] == needle:
    #         return i
    # return -1


def strStr(haystack, needle):
    j = 0
    i = 0
    # while j < len(needle) - 1:
    #     for k, v in enumerate(haystack):
    #         print(v, needle[j])
    #         if v == needle[j]:
    #             j += 1
    #         else:
    #             j = 0

    while i < len(haystack):
        while j < len(needle):
            if i < len(haystack):
                if haystack[i] == needle[j]:
                    j += 1
                    if j == len(needle) - 1:
                        return i - j + 1
                else:
                    j = 0
                i += 1
            else:
                return -1
    return -1

print(strStr('leetcode', 'leeto'))