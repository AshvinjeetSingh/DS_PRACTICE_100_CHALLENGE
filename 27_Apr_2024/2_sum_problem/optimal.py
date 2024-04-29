def twoSum(arr,target):
	arr.sort()
	i=0
	j=len(arr)-1
	# sum=0

	while i<len(arr) and j>0:
		if arr[i]+arr[j]<target:
			i+=1
		elif arr[i]+arr[j]>target:
			j-=1
		elif arr[i]+arr[j]==target:
			return [i,j]
	return -1

if __name__ == "__main__":
	arr=[2,6,5,4,11]
	target=14
	ans=twoSum(arr,target)
	print(ans)