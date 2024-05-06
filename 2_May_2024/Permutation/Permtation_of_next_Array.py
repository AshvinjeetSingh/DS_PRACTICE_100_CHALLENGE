def nextGreaterPermutation(arr):
    index=-1
    n=len(arr)

    for item in range(n-2,-1,-1):
        if arr[item]<arr[item+1]:
            index=item
            break
    if index==-1:
        arr.reverse()
        return arr

    for item in range(n-1,index,-1):
        if arr[item]>arr[index]:
            arr[item],arr[index]=arr[index],arr[item]
            break


    arr[index+1:]=reversed(arr[index+1:])

    return arr


if __name__ == "__main__":
    A = [2, 1, 5, 4, 3, 0, 0]
    ans = nextGreaterPermutation(A)

    print("The next permutation is: [", end="")
    for it in ans:
        print(it, end=" ")
    print("]")

    
# Time complexity:O(3N)
# Space Complexity:O(N) if reversed arr is considered other wise O(1)