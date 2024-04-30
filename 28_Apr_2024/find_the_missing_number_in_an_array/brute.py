def missingNumber(arr,n):
	for item in range(1,n+1):
		if item in arr:
			continue
		else:
			return item


if __name__ == "__main__":
	arr=[1,2,4,5]
	n=5
	result=missingNumber(arr,n)
	print(result)

	# Time complexity O(n)
	# Sapce complecity: O(1)