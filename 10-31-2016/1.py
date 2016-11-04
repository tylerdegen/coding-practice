def process(prices, profit):
	index = 0

	if len(prices) <= 1:
		return 0

	#assume first element is lowest
	low = prices[0]
	high = prices[1]
	test_profit = high - low
	for price in prices:
		if price > high:
			high = price
			temp_profit = high - low
			#is this test necessary
			#YES because now profit is passed in
			if temp_profit > profit:
				profit = temp_profit
				print ("profit gathered from " + str(high) + ", " + str(low))
		if price < low:
			temp_profit = process( prices[index: len(prices) - 1], profit )
			if temp_profit > profit:
				profit = temp_profit
				low = price
		index +=1
	return profit
	

	#handle decreasing price
	def process2(prices, profit):
	index = 1

	if len(prices) <= 1:
		return 0

	#assume first element is lowest
	bought = prices[0]
	sold = prices[1]
	profit = bought - sold
	
	while index < len(prices):
		test_profit = bought 
	
	for price in prices:
		if price > high:
			high = price
			temp_profit = high - low
			#is this test necessary
			#YES because now profit is passed in
			if temp_profit > profit:
				profit = temp_profit
				print ("profit gathered from " + str(high) + ", " + str(low))
		if price < low:
			temp_profit = process( prices[index: len(prices) - 1], profit )
			if temp_profit > profit:
				profit = temp_profit
				low = price
		index +=1
	return profit
			
def get_max_profit(stock_prices_yesterday):
	profit = 0
	low = stock_prices_yesterday[0]
	high = stock_prices_yesterday[0]
	profit = high - low
	'''
	for price in stock_prices_yesterday:
		if price < low:
			low = price
		if price > high:
			high = price
	return high - low
	'''
	
	'''
	index = 1
	#note -- don't need to bother checking last price, wouldn't buy at last minute
	while index < len(stock_prices_yesterday):
		price = stock_prices_yesterday[1]
		if price < low:
			temp_profit = process( stock_prices_yesterday[index: len(stock_prices_yesterday) - 1 ] )
			#process gets the max profit from that new low
			if temp_profit > profit:
				profit = temp_profit
		if price > high:
	'''	 

stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
#print get_max_profit(stock_prices_yesterday)
prices = [10, 9, 8, 7, 6]

#print process(stock_prices_yesterday, 0)
print("Testing negative prices", process(prices, -1))