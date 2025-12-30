def solution(n, words):
    used_words = {words[0]}
    last_word = words[0]
    
    for i, word in enumerate(words[1:], start=1):
        # 끝말잇기 규칙 확인
        if last_word[-1] != word[0] or word in used_words:
            player_no = i % n + 1
            turn_count = i // n + 1
            return [player_no, turn_count]
        
        used_words.add(word)
        last_word = word
    
    # 탈락자가 생기지 않은 경우
    return [0, 0]