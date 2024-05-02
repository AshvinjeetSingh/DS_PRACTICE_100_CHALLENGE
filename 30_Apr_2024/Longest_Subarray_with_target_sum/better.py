def longestSubarrayWithSumK(a, k) ->int :
    # Write your code here
    maxLen=0
    dict={}
    prefixSum=0
    n=len(a)
    for i in range(n):
        prefixSum=prefixSum+a[i]
        if prefixSum==k:
            maxLen=max(maxLen,i+1)
        rem=prefixSum - k
        if rem in dict:
            asd=i-dict[rem]
            maxLen=max(maxLen,asd)
        if prefixSum not in dict:
            dict[prefixSum]=i
    return maxLen
    pass



if __name__ == '__main__':
    a = [1, 2, 3, 1, 1, 1, 1]
    k = 3
    len = longestSubarrayWithSumK(a, k)
    print("The length of the longest subarray is:", len)


# time complexity:O(n)
# Space complexity :O(n)


