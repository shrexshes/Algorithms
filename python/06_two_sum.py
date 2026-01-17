from typing import List
def twoSum(nums:List[int],target:int):
    prevMap={} # this stores val: index
    
    for i,n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            print(f"result= {prevMap[diff]} , {i}")
            return [prevMap[diff],i]
        prevMap[n]=i
        print(f"index {prevMap[n]} {i}")
        return

twoSum([2,7,11,15],9)

