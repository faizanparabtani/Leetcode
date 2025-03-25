def longestMountain(arr):
	ret = 0

	for i in range(1, len(arr)-1):
		if arr[i-1] < arr[i] > arr[i+1]:
			l = r = i
			while l >= 0 and arr[l] > arr[l-1]:
				l -= 1

			while r <= len(arr) - 1 and arr[r] > arr[r+1]:
				r += 1

			ret = max(ret, r-l+1)

	return ret
	

def longestMountain(arr):
	longest = 0
    increase = 0
    decrease = 0
    for i in range(1, len(arr)):
        # Reset if the sequence is interrupted
        if (decrease and arr[i - 1] < arr[i]) or arr[i - 1] == arr[i]:
            increase = decrease = 0

        # Update increasing and decreasing sequences
        if arr[i - 1] < arr[i]:
            increase += 1
        elif arr[i - 1] > arr[i]:
            decrease += 1

        # Calculate mountain length if both sequences are active
        if increase != 0 and decrease != 0:
            longest = max(longest, increase + decrease + 1)
    return longest


arr = [2,1,4,7,3,2,5]
print(longestMountain(arr))