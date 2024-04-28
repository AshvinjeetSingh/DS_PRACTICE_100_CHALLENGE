def rotateArrayToRight(arr,size,rotation):

	reverseArray(arr,size-rotation,size)
	reverseArray(arr,0,size-rotation)
	reverseArray(arr,0,size)
	return arr


def rotateArrayToleft(arr,size,rotation):
	reverseArray(arr,0,rotation)
	reverseArray(arr,size-rotation-1,size)
	reverseArray(arr,0,size)
	return arr

def reverseArray(arr,start,stop):
	while start<stop:
		temp=arr[start]
		arr[start]=arr[stop-1]
		arr[stop-1]=temp
		start+=1
		stop-=1
	# print(arr)




if __name__ == "__main__":
	n=7
	arr=[1,2,3,4,5,6,7]
	k=3
	rightRotatedArray=rotateArrayToRight(arr,n,k)
	leftRotatedArray=rotateArrayToleft(arr,n,k)
	for item in rightRotatedArray:
		print(item," ",end="")
	for item in leftRotatedArray:
		print(item," ",end="")

# Time Complexity : O(n)
# Space Complexity : O(1)