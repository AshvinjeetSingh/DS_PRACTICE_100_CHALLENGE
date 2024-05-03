def printLeaders(arr,n):
    maxI=float("-inf")
    ans=[]

    for item in arr[::-1]:
        if item>maxI:
            ans.append(item)
        maxI=max(maxI,item)

    return ans
    pass


if __name__ == '__main__':
    # Array Initialization
    n = 6
    arr = [10, 22, 12, 3, 0, 6]

    ans = printLeaders(arr, n)

    for i in ans:
        print(i, end=" ")


# Time complexity:O(n)
# Space complexity:O(1)

