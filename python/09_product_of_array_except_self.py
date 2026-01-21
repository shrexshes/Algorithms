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
    postfix =[]
    prefix=[]

    for i,n in enumerate(nums):
        print("index at:",i)
        print("number at:",n)
        if i==0:
            postfix.append(n)
        else: postfix.append(n * postfix[i-1])
        print(postfix)

    x=nums(::-1)
    print(x)

productOfArray([1,2,3,4])
