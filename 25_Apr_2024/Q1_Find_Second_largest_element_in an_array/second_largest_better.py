def LargestElement(arr):
	largest=0
	for item in arr:
		if item >= largest:
			largest=item

	return largest

def secondLargestElement(arr):

	largest= LargestElement(arr)
	sLargest=0

	for item in arr:
		if item<largest and item>sLargest:
			sLargest=item

	return sLargest

if __name__ == '__main__':
    arr = [1, 2, 4, 6, 7, 5]
    value=secondLargestElement(arr)
    print(value) 


# Time Compexity:O(2n)
# Space Complexity :O(1)