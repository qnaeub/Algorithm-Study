def solution(record):
    answer = []
    user_db = {}
    msg = {'Enter': '님이 들어왔습니다.', 'Leave': '님이 나갔습니다.'}
    
    for r in record:
        action, uid, *nickname = r.split()
        if action in ['Enter', 'Change']:
            user_db[uid] = nickname[0]
    
    for r in record:
        action, uid, *nickname = r.split()
        if action in msg:
            answer.append(f"{user_db[uid]}{msg[action]}")
    
    return answer