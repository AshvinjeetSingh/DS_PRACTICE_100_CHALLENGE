def arrangeArray(arr):
	pos=[]
	neg=[]
	for item in arr:
		if item<0:
			neg.append(item)
		else:
			pos.append(item)

	i,j,k=0,0,0

	while k < len(arr):
		arr[k]=pos[i]
		k+=1
		i+=1
		arr[k]=neg[j]
		k+=1
		j+=1
	return arr

if __name__=="__main__":
	arr=[1,-1,2,-1,3,-1]
	array=arrangeArray(arr)
	for item in array:
		print(item,end=" ")

# space complexity:O(n)
# Time complexity :O(n) 
