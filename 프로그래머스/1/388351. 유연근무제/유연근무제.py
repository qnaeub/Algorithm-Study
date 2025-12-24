def solution(schedules, timelogs, startday):
    n = len(schedules)  # 전체 직원 수
    late = 0            # 지각 직원 수

    # 한 사람씩 지각 확인
    for i in range(n):
        # (i+1)번째 직원의 정상 출근 마감 시각 설정
        deadline = schedules[i] + 10
        if deadline % 100 >= 60:
            deadline += 40

        for j in range(7):
            # 주말인 경우 지각 체크 X
            today = (startday + j - 1) % 7 + 1
            if today >= 6:
                continue

            # (i+1)번째 직원이 지각한 경우, 지각 직원 수 1 증가
            if deadline < timelogs[i][j]:
                late += 1
                break

    # 전체 직원 수에서 지각 직원 수 제외
    answer = n - late
    return answer