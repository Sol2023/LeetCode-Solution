class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        maxleft=0
        maxright=0
        total_water=0
        while(left<right):
            if(height[left]<height[right]):
                if(height[left]>=maxleft):
                    maxleft=height[left]
                else:
                    total_water+=maxleft-height[left]
                left+=1
            else:
                if(height[right]>=maxright):
                    maxright=height[right]
                else:
                    total_water+=maxright-height[right]
                right-=1
        return total_water