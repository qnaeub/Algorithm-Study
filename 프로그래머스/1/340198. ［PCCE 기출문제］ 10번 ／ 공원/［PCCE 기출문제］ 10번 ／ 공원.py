def canPlace(i, j, m, park):
    for k in range(i, i+m):
        for l in range(j, j+m):
            if park[k][l] != "-1":
                return False
    return True

def solution(mats, park):
    mats = sorted(mats, reverse=True)
    answer = -1

    for i in range(len(park)):
        for j in range(len(park[0])):
            # 빈 공간 만나면 돗자리 큰 것부터 깔아보기
            if park[i][j] == "-1":
                for m in mats:
                    if i+m <= len(park) and j+m <= len(park[0]) and canPlace(i, j, m, park):
                            answer = max(answer, m)
                            break

    return answer