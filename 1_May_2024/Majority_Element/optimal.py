# This is also a moore algo approach

def majorityElement(nums):
	cnt=0
	maxCount=0
	elem=float('-inf')
	for item in nums:
		if cnt==0:
			count=1
			elem=item
		elif item==elem:
			count+=1
		else:
			count-=1
	for item in nums:
		if item==elem:
			maxCount+=1
	if maxCount>len(nums)/2:
		return elem

	return -1

if __name__=="__main__":
    arr= [2, 2, 1, 3, 1, 1, 3, 1, 1]
    majority_Elem=majorityElement(arr)
    print(majority_Elem)

# Time complexity:O(n)
# Sapce complexity:O(1)