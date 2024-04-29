def sortArray(arr,n):
	low=0
	mid=0
	high=n-1
	while mid<=high:
		if arr[mid]==0:
			arr[low],arr[mid]=arr[mid],arr[low]
			low+=1
			mid+=1
		elif arr[mid]==1:
			mid+=1
		elif arr[mid]==2:
			arr[high],arr[mid]=arr[mid],arr[high]
			high-=1

	return arr




if __name__ == "__main__":
	arr=[0, 2, 1, 2, 0, 1]
	n=len(arr)
	ans=sortArray(arr,n)
	for item in ans:
		print(item," ",end="")

# time complexity :O(n)
# space complexity : O(1)