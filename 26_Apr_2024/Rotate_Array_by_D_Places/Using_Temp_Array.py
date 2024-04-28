def RotateArrayToRight(arr,size,rotation):
	temp=[0]*rotation
	for item in range(size-rotation-1,size):
		temp[item-size+rotation] = arr[item]

	for item in range(size,rotation,-1):
		arr[item-1] =arr[item-rotation-1]

	for item in range(k):
		arr[item]=temp[item]

	return arr
	pass

def RotateArrayToLeft(arr,size,rotation):
	temp=[0]*rotation
	for item in range(rotation):
		temp[item]=arr[item]
	for item in range(0,size-rotation):
		arr[item]= arr[item+rotation]
	for item in range(size-rotation,size):
		arr[item]=temp[item-size+rotation]

	return arr
	pass

if __name__ == "__main__":
	n=7
	arr=[1,2,3,4,5,6,7]
	k=2
	RightRotatedArray=RotateArrayToRight(arr,n,k)
	LeftRotatedArray=RotateArrayToLeft(arr,n,k)
	for item in RightRotatedArray:
		print(item," ",end="")
	for item in LeftRotatedArray:
		print(item," ",end="")



# Time Complexity O(3n)
# Space Complexity O(n)