import math

def solution(n,a,b):
    turn = 0
    
    while a != b:
        a, b = math.ceil(a / 2), math.ceil(b / 2)
        turn += 1
        
    return turn