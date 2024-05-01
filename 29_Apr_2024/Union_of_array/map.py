
def  unionOfArray(arr1,arr2):
	freq={}
	final=[]

	for item in arr1:
		freq[item]=freq.get(item,0)+1

	for item in arr2:
		freq[item]=freq.get(item,0)+1

	for item in freq:
		final.append(item)

	return final



if __name__ == "__main__":
	arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	arr2 = [2, 3, 4, 4, 5, 11, 12]
	final=unionOfArray(arr1,arr2)
	for item in final:
		print(item,end=" ")



# Time complexity : O((m+n)logn)
# Space complexity : O(m+n)