def sortArray(arr1,arr2):
	left=len(arr1)-1
	right=0
	while left>0 and right<len(arr2):
		if arr1[left]>arr2[right]:
			arr1[left],arr2[right]=arr2[right],arr1[left]
			left-=1
			right+=1
		elif arr1[left]<arr2[right]:
			break

	arr1.sort()
	arr2.sort()
	i=0
	while i<len(arr2):
		arr1.append(arr2[i])
		i+=1

	return arr1




if __name__ == "__main__":
	arr1=[1,1,2,3,5]
	arr2=[1,4,6,8,9]
	
	ans=sortArray(arr1,arr2)
	for item in ans:
		print(item," ",end="")

# both the arrays should be sorted
# time complexity :O(nlogn)
# space compleity:O(1)