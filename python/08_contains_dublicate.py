from typing import List
def containsDuplicate(nums:List[int])->bool:
    '''
    Input: nums = [1,2,3,1]

    Output: true

    Explanation:
        The element 1 occurs at the indices 0 and 3.
    '''
    hashMap=set()
    for n in nums:
        if n in hashMap:
            print(True)
            return True

        hashMap.add(n)
    print(False)
    return False 
containsDuplicate([1,2,3,1])
