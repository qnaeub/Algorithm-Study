def solution(wallet, bill):
    wallet_min, wallet_max = sorted(wallet)
    bill_min, bill_max = sorted(bill)
    answer = 0
    
    while (bill_min > wallet_min or bill_max > wallet_max):
        bill_max //= 2
        bill_min, bill_max = sorted([bill_min, bill_max])
        answer += 1
    
    return answer