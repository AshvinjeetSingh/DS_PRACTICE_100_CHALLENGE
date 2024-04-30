def missingNumber(arr,n):
	dict={item:0 for item in range(n+1)}

	for item in arr:
		if item in dict:
			dict[item]+=1
	for item in range(1,n+1):
		if dict[item]==0:
			return item



if __name__ == "__main__":
	arr=[1,2,3,4,5,6]
	n=7
	result=missingNumber(arr,n)
	print(result)


# Time complexity:O(N)
# Space complexity:O(N)