def time_to_seconds(time_str):
    # 초 단위로 변환
    m, s = map(int, time_str.split(":"))
    return m * 60 + s

def seconds_to_time(total_seconds):
    # 00:00 형식으로 변환
    m, s = divmod(total_seconds, 60)
    return f"{m:02d}:{s:02d}"

def solution(video_len, pos, op_start, op_end, commands):
    # 초 단위로 변환
    video_len_s = time_to_seconds(video_len)
    pos_s = time_to_seconds(pos)
    op_start_s = time_to_seconds(op_start)
    op_end_s = time_to_seconds(op_end)
    
    # 현재 위치가 오프닝 구간일 경우, 오프닝 끝나는 위치로 이동
    def skip_opening(current):
        if op_start_s <= current <= op_end_s:
            return op_end_s
        return current
    
    # 처음 위치 체크
    pos_s = skip_opening(pos_s)
    
    for c in commands:
        # prev: 10초 전으로 이동, next: 10초 후로 이동
        # 동영상 범위 밖인 경우, 영상의 처음 또는 마지막 위치로 이동
        if c == "prev":
            pos_s = max(0, pos_s - 10)
        else:
            pos_s = min(video_len_s, pos_s + 10)

        # 명령 수행 후 오프닝 위치 체크
        pos_s = skip_opening(pos_s)
    
    # 00:00 형식으로 반환
    return seconds_to_time(pos_s)