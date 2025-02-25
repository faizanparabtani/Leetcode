def minTimeToVisitAllPoints(points):
    """
    :type points: List[List[int]]
    :rtype: int
    """

    if len(points) == 1:
        return 0

    i = 0
    j = 1
    result = 0
    while j < len(points):
        time_to_visit = max(abs((points[i][0] - points[j][0])), abs((points[i][1] - points[j][1])))
        result += time_to_visit
        j += 1
        i += 1
    return result




points = [[1,1],[3,4],[-1,0]]
ans = minTimeToVisitAllPoints(points)
print(ans)