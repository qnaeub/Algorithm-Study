def solution(k, m, score):
    score.sort(reverse=True)
    return sum(score[m-1::m]) * m