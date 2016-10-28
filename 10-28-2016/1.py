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
    
    i = 0
    test_num = 0
    while i <= len:
    	test_num += digits[i] * 10**i
    	i+=1
    print test_num
    
    possible = []
    i = 0
    
    while i < len:
    	#this gets each answer
    	result = 0
    	index = 0
    	j = 0
    	#this gets each digit of each answer
    	while index <= len:
    		digit = digits[index]
    		if index == i:
    			digit += digits[index+1]
    			if digit % 2 == 1:
    				digit += 1
    			digit /= 2
    			index += 1
    		result += digit * 10**j
    		j += 1
    		index += 1
    	possible.append(result)
    	i += 1
    print possible
    print max(possible), "\n"
    		


solution(43)
solution(526)
solution(623315)
