def  sortArray(arr1,n,arr2,m):
	last =n+m-1
	while n>0 and m>0:
		if arr1[n-1]>arr2[m-1]:
			arr1[last]=arr1[n-1]
			n-=1
		elif arr1[n-1]<arr2[m-1]:
			arr1[last]=arr2[m-1]
			m-=1
		last-=1
	while n>0:
		arr1[last]=arr1[n-1]
		last-=1
		n-=1
	while m>0:
		arr1[last]=arr2[m-1]
		last-=1
		m-=1
	return arr1
	pass



if __name__ == "__main__":
	arr1=[1, 2, 3, 0, 0, 0]
	arr2=[4,5,6]
	n=3
	m=3
	ans=sortArray(arr1,n,arr2,m)
	for item in ans:
		print(item," ",end="")