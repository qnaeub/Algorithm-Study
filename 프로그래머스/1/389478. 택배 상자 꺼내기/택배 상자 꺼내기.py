def solution(n, w, num):
    # 상자 번호의 인덱스
    r_index = 0
    c_index = 0
    
    # 행 개수 설정
    r = (n + w - 1) // w

    # 0으로 채운 행렬 생성
    matrix = [[0] * w for _ in range(r)]

    # 상자 쌓기
    isReverse = True
    k = 0
    for i in range(r - 1, -1, -1):
        isReverse = not isReverse
        # 정방향 쌓기
        if isReverse == False:
            for j in range(w):
                k += 1
                if k > n:
                    break
                matrix[i][j] = k
                if k == num:
                    r_index = i
                    c_index = j
        # 역방향 쌓기
        else:
            for j in range(w - 1, -1, -1):
                k += 1
                if k > n:
                    break
                matrix[i][j] = k
                if k == num:
                    r_index = i
                    c_index = j

    # 꺼내야 하는 상자 개수 세기
    answer = 0
    for i in range(r_index + 1):
        if matrix[i][c_index] == 0:
            continue
        elif i > r_index:
            break
        else:
            answer += 1

    return answer