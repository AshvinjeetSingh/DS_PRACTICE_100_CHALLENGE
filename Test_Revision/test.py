def lenOfLongSubarr (arr, n, k) : 
        #Complete the function
        dic={0:1}
        prefixSum=0
        cnt=0
        for item in range(n):
            prefixSum+=arr[item]
            rem=prefixSum-k
            if rem in dic:
                cnt+=dic[rem]
            dic[prefixSum]+=1
        return cnt


if __name__=="__main__":
    arr=[0,0,0,0,0,0,0,0,0,0]
    target=0
    n=len(arr)
    ans=lenOfLongSubarr(arr,n,target)
    print(ans)

