def solution(wallet, bill):
    wallet, bill = sorted(wallet), sorted(bill)
    answer = 0
    
    while (bill[0] > wallet[0] or bill[1] > wallet[1]):
        bill[1] //= 2
        bill = sorted(bill)
        answer += 1
    
    return answer