def unionOfArray(arr1,arr2):
	i,j,index=0,0,0
	n,m=len(arr1),len(arr2)
	final=[]
	
	while i<n and j<m:
		if arr1[i] <= arr2[j]:
			if len(final)==0 or final[index-1]!=arr1[i]:
				final.append(arr1[i])
				index+=1
			i+=1
		else:
			if len(final)==0 or final[index-1]!=arr2[j]:
				final.append(arr2[j])
				index+=1
			j+=1



	while i<n:
		if final[index-1]!=arr1[i]:
			final.append(arr1[i])
			index+=1
		i+=1

	while j<m:
		if final[index-1]!=arr2[j]:
			final.append(arr2[j])
			index+=1
		j+=1
	return final



if __name__ == "__main__":
	arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	arr2 = [2, 3, 4, 4, 5, 11, 12]
	final=unionOfArray(arr1,arr2)
	for item in final:
		print(item,end=" ")

# Time complexity : O(m+n)
# Space complexity:O(n)
