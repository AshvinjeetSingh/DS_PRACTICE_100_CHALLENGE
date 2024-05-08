def subArrayWithMaxSumPosition(arr):
	maxSum=arr[0]
	currentSum=arr[0]
	startingPos=-1
	endingPos=-1
	for item in range(1,len(arr)):
		if currentSum<0:
			start=item
			
		currentSum=max(currentSum+arr[item],arr[item])
		if currentSum>=maxSum:
			startingPos=start
			endingPos=item
		maxSum=max(maxSum,currentSum)
		
	return [startingPos,endingPos]
	pass

if __name__=="__main__":
	arr=[-2, 1, -3, 4, -1, 2, 1, -5, 4]
	position=subArrayWithMaxSumPosition(arr)
	for item in range(position[0],position[-1]+1):
		print(arr[item],end=" ")
