def kadanesAlgo(arr):
	maxSum=0
	maxI=float('-inf')

	for item in range(len(arr)):
		maxSum+=arr[item]

		if maxSum>maxI:
			maxI=maxSum
		if maxSum<0:
			maxSum=0

	return maxI



if __name__ == "__main__":
	arr = [-2,1,-3,4,-1,2,1,-5,4] 
	result=kadanesAlgo(arr)
	print(result)