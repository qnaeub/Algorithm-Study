def solution(n, words):
    # 첫 번째 단어가 한 글자인 경우
    if len(words[0]) == 1:
        return [1, 1]
    
    # 끝말잇기 규칙 확인
    for i in range(1, len(words)):
        for j in range(i):
            if (words[j] == words[i]) or (len(words[i]) == 1) or (words[i-1].strip()[-1] != words[i].strip()[0]):
                return [i % n + 1, i // n + 1]
    
    # 탈락자가 생기지 않은 경우
    return [0, 0]