def maxProfit(arr):
	n=len(arr)
	maxProfit=-1
	for i in range(0,n):
		for j in range(i,n):
			if arr[j]-arr[i] > maxProfit and arr[j]>arr[i]:
				maxProfit=arr[j]-arr[i]


	if maxProfit <0 :
		return 0

	return maxProfit



if __name__ == "__main__":
	arr = [7, 1, 5, 3, 8, 4]
	maxPro = maxProfit(arr)
	print("Max profit is:", maxPro)



# Time complexity:O(N^2)
# Space complexity:O(1)