import math

def solution(X):
    digits = []

    len = math.floor(math.log(X, 10))
    #get each individual digit
    i = 0
    while i <= len:
        digit = X%10**(i+1) - X%10**i
        digit /= 10**i
        digits.append(digit)
        i += 1
    print digits


solution(43)
solution(526)
