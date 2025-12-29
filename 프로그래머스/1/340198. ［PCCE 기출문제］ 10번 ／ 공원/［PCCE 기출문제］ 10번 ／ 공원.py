def canPlace(park, mats):
    for m in mats:
        for i in range(len(park)):
            for j in range(len(park[0])):
                if i+m <= len(park) and j+m <= len(park[0]) and all(park[k][l] == "-1" for k in range(i, i+m) for l in range(j, j+m)):
                                return m
    return -1

def solution(mats, park):
    mats = sorted(mats, reverse=True)
    answer = canPlace(park, mats)

    return answer