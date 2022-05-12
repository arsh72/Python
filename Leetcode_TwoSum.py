class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans=[]
        indexmap={}
        for i,num in enumerate(nums):
            diff = target-num
            if(diff in indexmap):
                return [indexmap[diff],i]
            else:
                indexmap[num]=i
        
            
        