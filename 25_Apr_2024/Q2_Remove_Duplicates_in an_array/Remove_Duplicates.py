def RemoveDupicates(arr):
	newSet =set()
	for item in arr:
		newSet.add(item)

	j=0
	lengthSet=len(newSet)
	for item in  newSet:
		arr[j]=item
		j+=1
	return lengthSet



if __name__== "__main__":
	arr=[1,1,1,2,2,3,3,3,3,4,4]
	length=RemoveDupicates(arr)
	for item in range(length):
		print(arr[item]," ",end="")



