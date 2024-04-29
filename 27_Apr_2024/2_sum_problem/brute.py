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