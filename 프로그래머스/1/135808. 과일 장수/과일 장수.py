def solution(k, m, score):
    score.sort(reverse=True)
    score = [score[i:i+m] for i in range(0, len(score), m)]
    if len(score[-1]) < m:
        del score[-1]

    answer = 0
    for i in range(len(score)):
        answer += score[i][-1] * m
        
    return answer