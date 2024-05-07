def maxProfit(arr):
	profit=0
	minValue=arr[0]

	for item in range(1,len(arr)):
		cost = arr[item]-minValue
		profit=max(profit,cost)
		minValue=min(arr[item],minValue)

	if profit <0:
		return 0

	return profit
if __name__ == "__main__":
	arr = [7, 1, 5, 3, 6, 4]
	maxPro = maxProfit(arr)
	print("Max profit is:", maxPro)



# Time complexity:O(N)
# Space complexity:O(1)