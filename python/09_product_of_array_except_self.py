from typing import List
def productOfArray(nums:List[int])->int:
    '''
    Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
    You must write an algorithm that runs in O(n) time and without using the division operation.
    
    Example 1:
        Input: nums = [1,2,3,4]
        Output: [24,12,8,6]

    Personal View:
        So here we get a list of nums , now we have to see this problem in a different way [1,2,3,4]
        1st we do postfix : multiplying every number in a list from left to right [1,2,6,24]
        2nd we do prefix : multiplying every number in a list from right to left [24,24,12,4]
        3rd we take another list and we take the the value that comes befor it in prefix and take a value that comes after it in a postfix [24,12,8,6] 
    '''

    res=[1] * len(nums)# res=4
    prefix=1
    for i in range(len(nums)): #i=0,i=1,i=2
        res[i]=prefix # prefix=1 ,1,2,6
        print(res)
        prefix *= nums[i] #prefix=1*1, prefix=1*2 , prefix=2*3,prefix=6*4 stop
    print(res)
    postfix=1
    for i in range(len(nums)-1,-1,-1):
        res[i] *= postfix # res[3]=6 * 1 , res[2]=2*4, res[1]=1*12, res[0]=1*24
        print("postfix res",res) # 6 ,8,12,24
        postfix *= nums[i] #1 * 4=4,4*3=12, 12*2 =24,24*1=24
        print(postfix)

productOfArray([1,2,3,4])

