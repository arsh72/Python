class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a=set()
        for num in nums:
            a.add(num)
        if(len(a)==len(nums)):
            return False
        else:
            return True