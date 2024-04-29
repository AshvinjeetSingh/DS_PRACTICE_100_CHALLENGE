
def sortArray(arr,n):
	cnt0=0
	cnt1=0
	cnt2=0
	index=0
	for item in arr:
		if item ==0:
			cnt0+=1
		elif item==1:
			cnt1+=1
		else:
			cnt2+=1

	
	while index<n:
		if cnt0!=0:
			arr[index]=0
			index+=1
			cnt0-=1
		elif cnt1!=0:
			arr[index]=1
			index+=1
			cnt1-=1
		elif cnt2!=0:
			arr[index]=2
			index+=1
			cnt2-=1




if __name__ == "__main__":
	arr=[0, 2, 1, 2, 0, 1]
	n=len(arr)
	ans = sortArray(arr,n)
	print(sorted_keys)
	for item in ans:
		print(item," ",end="")


# time complexity:O(2n)
# Space complexity:O(1)


