def canPlace(park, mats):
    r, c = len(park), len(park[0])
    
    for m in mats:
        # 돗자리 길이가 공원 길이보다 더 길면 건너뛰기
        if m > r or m > c:
            continue

        for i in range(r - m + 1):
            for j in range(c - m + 1):
                # 빈 공간 만나면 돗자리 깔 수 있는지 확인
                if park[i][j] == "-1":
                    if all(park[k][l] == "-1" for k in range(i, i+m) for l in range(j, j+m)):
                        return m

    return -1

def solution(mats, park):
    # 돗자리 길이 긴 순서대로 정렬
    return canPlace(park, sorted(mats, reverse=True))