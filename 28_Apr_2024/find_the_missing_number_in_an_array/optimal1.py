def missingNumber(arr,n):
	arraySum=int(n*(n+1)/2)
	Sum=0
	for item in arr:
		Sum=Sum+item

	return arraySum-Sum


if __name__ == "__main__":
	arr=[1,2,3,4,5,6]
	n=7
	result=missingNumber(arr,n)
	print(result)


# Time complexity:O(N)
# Space complexity:O(1)