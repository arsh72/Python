class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        a=[]
        for i,num in enumerate(nums):
            if i>0 and num==nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            while(l<r):
                if(nums[l]+nums[r]>0-nums[i]):
                    r-=1
                elif(nums[l]+nums[r]<0-nums[i]):
                    l+=1
                else:
                    a.append([nums[i],nums[l],nums[r]])
                    r-=1
                    while(nums[r]==nums[r+1] and l<r):
                        r-=1
        return a
                             
                             
