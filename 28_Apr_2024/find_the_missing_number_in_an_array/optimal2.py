def missingNumber(arr,n):
	xor1=0
	xor2=0
	for item in range(1,n+1):
		xor1=xor1^item

	for item in arr:
		xor2=xor2^item

	return xor1^xor2


if __name__ == "__main__":
	arr=[1,2,3,4,5,6]
	n=7
	result=missingNumber(arr,n)
	print(result)



# Time complexity:O(N)
# Space complexity:O(1)