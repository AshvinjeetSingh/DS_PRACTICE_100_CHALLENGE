def secondLargestElement(arr):
	largest=arr[0]
	sLargest=0

	for item in range(1,len(arr)):
		if arr[item] >largest:
			sLargest=largest
			largest = arr[item]

		if arr[item] >  sLargest and arr[item]< largest:
			sLargest = arr[item]

	return sLargest


if __name__ == '__main__':
    arr = [1, 2, 4, 6, 7, 5]
    value=secondLargestElement(arr)
    print(value) 


# time complexity:O(n)
# Space complexity:O(1)