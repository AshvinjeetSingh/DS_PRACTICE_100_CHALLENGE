def getSingleElement(arr):
    dict={item:0 for item in arr}

    for item in arr:
        if item in dict:
            dict[item]+=1

    for key,values in dict.items():
        if values==1:
            return key
    pass

if __name__ == "__main__":
    arr = [4, 1, 2, 1, 2]
    ans = getSingleElement(arr)
    print("The single element is:", ans)


# Time complexity:O(N+M)
# Space Complexity:O(N)
