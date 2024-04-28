def moveZeroesToEnd(arr,n):
	i=0
	j=0

	for item in range(0,n):
		if arr[item]==0:
			j=item
			i=j+1
			break
	while i<n:
		if arr[i] !=0:
			arr[i],arr[j]=arr[j],arr[i]
			j+=1
		i+=1
	return arr




if __name__ == "__main__":
	arr=[1, 0, 2, 3, 2, 0, 0, 4, 5, 1]
	n=len(arr)
	finalArray=moveZeroesToEnd(arr,n)
	for item in finalArray:
		print(item," ",end="")

# Time complexity :O(n)
# Space Complexity:O(1)