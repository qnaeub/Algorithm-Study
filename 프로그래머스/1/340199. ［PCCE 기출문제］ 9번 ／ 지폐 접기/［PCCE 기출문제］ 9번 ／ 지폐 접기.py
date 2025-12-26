def solution(wallet, bill):
    answer = 0
    
    while (min(bill) > min(wallet) or max(bill) > max(wallet)):
        bill[bill.index(max(bill))] //= 2
        answer += 1
    
    return answer