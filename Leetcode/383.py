from collections import Counter

# def canConstruct(ransomNote, magazine):
#     ransomNote_counter = Counter(ransomNote)
#     magazine_counter = Counter(magazine)

#     for i in ransomNote_counter:
#         if i not in magazine_counter: return False
#         if ransomNote_counter[i] <= magazine_counter[i]:
#             continue
#         else:
#             return False

#     return True


def canConstruct(ransomNote, magazine):
    ran_point = mag_point = 0

    if len(ransomNote) > len(magazine):
        return False
    
    while mag_point < len(magazine):
        if ransomNote[ran_point] != magazine[mag_point]:
            mag_point += 1
            continue
        
        ran_point += 1
        mag_point += 1

    return True

ransomNote = "aab"
magazine = "baa"
print(canConstruct(ransomNote, magazine))