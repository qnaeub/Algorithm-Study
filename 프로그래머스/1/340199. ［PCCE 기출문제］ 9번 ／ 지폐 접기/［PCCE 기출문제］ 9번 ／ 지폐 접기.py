def solution(wallet, bill):
    # 정렬된 값으로 변수 할당
    w_min, w_max = sorted(wallet)
    b_min, b_max = sorted(bill)
    answer = 0
    
    while b_min > w_min or b_max > w_max:
		# 길이가 긴 쪽 반으로 접기
        b_max //= 2
        
        # 재정렬
        if b_min > b_max:
	        b_min, b_max = b_max, b_min
            
        answer += 1
    
    return answer