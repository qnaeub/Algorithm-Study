def ms(t):
    # 숫자로 변환
    m, s = t.split(":")
    return int(m) * 100 + int(s)

def solution(video_len, pos, op_start, op_end, commands):
    # 숫자로 변환
    video_len_ms = ms(video_len)
    pos_ms = ms(pos)
    op_start_ms = ms(op_start)
    op_end_ms = ms(op_end)
    
    # 오프닝 구간일 경우, 오프닝 끝나는 위치로 이동
    if op_start_ms <= pos_ms < op_end_ms: pos_ms = op_end_ms
    
    for c in commands:
        # prev: 10초 전으로 이동, next: 10초 후로 이동
        if c == "prev":
            pos_ms -= 10
            if pos_ms % 100 >= 60:
                pos_ms -= 40
        else:
            pos_ms += 10
            if pos_ms % 100 >= 60:
                pos_ms += 40

        # 동영상 범위 밖인 경우, 영상의 처음 또는 마지막 위치로 이동
        if pos_ms < 0:
            pos_ms = 0
        elif pos_ms > video_len_ms:
            pos_ms = video_len_ms
            
        # 오프닝 구간일 경우, 오프닝 끝나는 위치로 이동
        if op_start_ms <= pos_ms < op_end_ms: pos_ms = op_end_ms
    
    # 00:00 형식으로 반환
    return f"{str(pos_ms//100).zfill(2)}:{str(pos_ms%100).zfill(2)}"