from typing import List
def twoSum(nums:List[int],target:int):
    prevMap={} # this stores val: index
    for i , n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            result=[prevMap[diff],i]
            print(result)
            return result
        prevMap[n]=i
    return []

twoSum([10,20,30,50],40)
