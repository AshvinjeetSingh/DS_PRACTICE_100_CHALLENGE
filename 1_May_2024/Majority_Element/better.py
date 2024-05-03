def majorityElement(nums):
    
    dict={item:0 for item in nums}

    for item in nums:
        if item in dict:
            dict[item]+=1
        

    for key,value in dict.items():
        if value>len(nums)/2:
            return key
        
    return -1



if __name__=="__main__":
    arr=[1,2,1,2,2,1]
    majority_Elem=majorityElement(arr)
    print(majority_Elem)

# Time complexity:O(nlogn+n)
# Sapce complexity:O(n)