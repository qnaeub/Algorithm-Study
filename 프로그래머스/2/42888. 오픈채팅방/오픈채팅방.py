def solution(record):
    answer = []
    ulist = {}
    
    for r in record:
        r = r.split(' ')
        if r[0] == "Enter":
            ulist[r[1]] = r[2]
        if r[0] == "Change":
            ulist[r[1]] = r[2]
    
    for r in record:
        r = r.split(' ')
        if r[0] == "Enter":
            answer.append(f"{ulist[r[1]]}님이 들어왔습니다.")
        elif r[0] == "Leave":
            answer.append(f"{ulist[r[1]]}님이 나갔습니다.")
    
    return answer