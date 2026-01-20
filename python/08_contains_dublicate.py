from typing import List
def containsDuplicate(nums:List[int])->bool:
    hashMap=set()
    for n in nums:
        if n in hashMap:
            print(True)
            return True

        hashMap.add(n)
    print(False)
    return False 
containsDuplicate([1,2,3,1])
