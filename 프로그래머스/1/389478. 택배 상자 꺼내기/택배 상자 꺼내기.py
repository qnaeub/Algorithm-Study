def solution(n, w, num):
    # 상자 번호의 인덱스
    r_index = (num - 1) // w
    c_index = (num - 1) % w
    if r_index % 2 != 0:
        c_index = (w - 1) - c_index
    
    # 행 개수 설정
    r = (n + w - 1) // w

    # 0으로 채운 행렬 생성
    matrix = [[0] * w for _ in range(r)]

    # 상자 쌓기
    k = 0
    for i in range(r):
        for j in range(w):
            k += 1
            if k > n: break
            
            real_j = j if i % 2 == 0 else (w - 1) - j
            
            matrix[i][real_j] = k

    # 꺼내야 하는 상자 개수 세기
    answer = 0
    for i in range(r_index, r, 1):
        if matrix[i][c_index] != 0:
            answer += 1
        else:
            break

    return answer