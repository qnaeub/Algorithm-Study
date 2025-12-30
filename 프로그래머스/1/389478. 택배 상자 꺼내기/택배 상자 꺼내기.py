def solution(n, w, num):
    # 정방향 + 역방향 = 2w
    m1 = num % (2 * w)
    m2 = (2 * w + 1 - m1) % (2 * w)
    offset = (m2 - m1) % (2 * w)

    # 꺼내야 하는 상자 개수 세기
    answer = 0
    # num과 같은 방향 상자 개수 세기
    answer += len(range(num, n + 1, 2 * w))
    # num과 다른 방향 상자 개수 세기
    if offset > 0:
        answer += len(range(num + offset, n + 1, 2 * w))

    return answer