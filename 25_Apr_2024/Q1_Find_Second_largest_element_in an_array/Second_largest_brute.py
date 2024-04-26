def secondLargestElement (arr,size):
	arr.sort()
	return arr[-2]


if __name__ == '__main__':
    arr = [1, 2, 4, 6, 7, 5]
    n = len(arr)
    value=secondLargestElement(arr, n)
    print(value)



    # Time complexity  O(nlogn)
    # Space Complexity  O(1)