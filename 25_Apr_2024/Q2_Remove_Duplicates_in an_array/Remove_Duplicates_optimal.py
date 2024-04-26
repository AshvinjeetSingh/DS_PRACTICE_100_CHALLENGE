def removeDuplicate(arr):
	i=0;j=1

	for item in range(1,len(arr)):

		if arr[i]!=arr[j]:
			arr[i+1]=arr[j]
			i+=1

		j+=1
	return i+1


if __name__ == "__main__":
	arr=[1,1,1,2,2,3,3,3,3,4,4]
	dupe= removeDuplicate(arr)
	for item in range(dupe):
		print(arr[item]," ",end="")


# time complexity O(n)
# Space complexity O(1)





