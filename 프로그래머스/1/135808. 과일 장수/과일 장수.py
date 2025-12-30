def solution(k, m, score):
    answer, i = 0, 0
    score.sort(reverse=True)
    
    while i < len(score) - (len(score) % m):
        answer += score[i + m - 1] * m
        i += m
        
    return answer