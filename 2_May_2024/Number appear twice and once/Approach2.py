def getSingleElement(arr):
    XOR=0
    for item in arr:
        XOR=XOR^item

    return XOR



if __name__ == "__main__":
    arr = [4, 1, 2, 1, 2]
    ans = getSingleElement(arr)
    print("The single element is:", ans)


# Time complexity:O(N)
# Space Complexity:O(1)