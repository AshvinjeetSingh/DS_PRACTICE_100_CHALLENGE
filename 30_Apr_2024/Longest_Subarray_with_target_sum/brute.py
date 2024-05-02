def longestSubarrayWithSumK(a, k) ->int :
    # Write your code here
    maxLen=0
    
    for i in range(len(a)):
        prefixSum=0
        for j in range(i,len(a)):
            prefixSum = prefixSum+a[j]
            if prefixSum==k:
                maxLen=max(maxLen,j-i+1)
    return maxLen
    pass



if __name__ == '__main__':
    a = [1, 2, 3, 1, 1, 1, 1]
    k = 3
    len = longestSubarrayWithSumK(a, k)
    print("The length of the longest subarray is:", len)


# Time complexity:O(n^2)
# Space complexity:O(1)




