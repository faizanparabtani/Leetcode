def jumpingOnClouds(c):
    i = 0
    jump = 0
    buffer_lis = []
    while(i <= len(c)):
        if len(buffer_lis) < 4:
            if c[i] == 0:
                buffer_lis.append(c[i])
            else:
                jump += 1
                i+= 2
        else:
            jump += 2
            i+= 1
    return jump


ans = jumpingOnClouds([0, 0, 1, 0, 0, 1, 0])
print(ans)