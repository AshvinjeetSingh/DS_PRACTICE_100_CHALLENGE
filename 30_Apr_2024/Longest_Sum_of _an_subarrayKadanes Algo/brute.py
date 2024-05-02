def kadanesAlgo(arr):
	maxSum=0
	for i in range(len(arr)):
		tempSum=0
		for j in range(i,len(arr)):
			tempSum=tempSum+arr[j]

			if tempSum>maxSum:
				maxSum=tempSum

	return maxSum


if __name__ == "__main__":
	arr = [-2,1,-3,4,-1,2,1,-5,4] 
	result=kadanesAlgo(arr)
	print(result)