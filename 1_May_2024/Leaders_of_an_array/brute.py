def printLeaders(arr,n):
    maxI=float("-inf")
    ans=[]
    
    for i in range(0,n):
        flag=True
        for j in range(i,n):
            if arr[j]>arr[i]:
                flag=False
                break
            else:
                continue
        if flag:
            ans.append(arr[i])


    return ans
    pass


if __name__ == '__main__':
    # Array Initialization
    n = 6
    arr = [10, 22, 12, 3, 0, 6]

    ans = printLeaders(arr, n)

    for i in ans:
        print(i, end=" ")


# Time complexity:O(n^2)
# Space complexity:O(n)