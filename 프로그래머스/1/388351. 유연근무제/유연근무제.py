def solution(schedules, timelogs, startday):
    n = len(schedules)  # 전체 직원 수
    late = 0            # 지각 직원 수

    # 한 사람씩 지각 확인
    for i in range(n):
        # 출근 희망 시각 -> 출근 가능 시각으로 조정
        schedules[i] += 10
        if schedules[i] % 100 > 59:
            schedules[i] += 40
            
        today = startday - 1

        for j in range(7):
            # 주말인 경우 지각 체크 X
            today += 1
            if today > 7:
                today = 1
            elif (today == 6) | (today == 7):
                continue

            # 지각자 수 체크
            if schedules[i] < timelogs[i][j]:
                late += 1
                break
            else:
                j += 1

        i += 1

    # 전체 인원에서 지각자 수 제외
    answer = n - late
    return answer