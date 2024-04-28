def  moveZeroesToEnd(arr,n):
	temp=[]
	for item in arr:
		if item!=0:
			temp.append(item)

	for item in range(n-len(temp)):
		temp.append(0)

	return temp
	pass

if __name__ == "__main__":
	arr=[1, 0, 2, 3, 2, 0, 0, 4, 5, 1]
	n=len(arr)
	finalArray=moveZeroesToEnd(arr,n)
	for item in finalArray:
		print(item," ",end="")


# Time complexity:O(n)
# Space Complexity:O(n)



