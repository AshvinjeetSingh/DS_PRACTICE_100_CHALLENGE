def twoSum(arr,target):
	for item in arr:
		if target-item in arr:
			return [arr.index(item),arr.index(target-item)]
		else:
			continue
if __name__ == "__main__":
	arr=[2, 6, 5, 8, 11]
	target=14
	ans=twoSum(arr,target)
	print(ans)

	# time compelxity:O(n^2) 
	# The code has a nested loop structure where for
	# each element in the input array 'arr', it checks if the difference
	# between the target and the current element is present in the array.
	# This results in a quadratic time complexity as in the worst case
	# scenario, each element in the array is compared with every other
	# element in the array

	# space complexity:O(1)