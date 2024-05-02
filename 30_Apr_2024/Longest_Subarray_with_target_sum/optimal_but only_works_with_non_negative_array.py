def longestSubarrayWithSumK(a, k) ->int :
    left=0
    right=0
    pSum=a[0]
    maxLen=0

    while right<len(a):
        while left<=right and pSum>k:
            pSum-=a[left]
            left+=1

        if pSum==k:
            maxLen=max(maxLen,right-left+1)
        right+=1
        if right<len(a):
            
            pSum+=a[right]
    return maxLen




if __name__ == '__main__':
    a = [1, 2, 3, 1, 1, 1, 1]
    k = 3
    len = longestSubarrayWithSumK(a, k)
    print("The length of the longest subarray is:", len)


    # this one only works for positives
    # for other cases better is the optimal 1
    # Time complexity:O(n)
    # Space complexity:O(1)