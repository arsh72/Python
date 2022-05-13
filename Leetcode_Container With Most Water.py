class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        res = (r-l)*min(height[r],height[l])
        while(l<r):
            if(height[l]<=height[r]):
                l+=1
            elif(height[r]<height[l]):
                r-=1
            area = (r-l)*min(height[r],height[l])
            res=max(res,area)
        return res
                
                
            
            
        
