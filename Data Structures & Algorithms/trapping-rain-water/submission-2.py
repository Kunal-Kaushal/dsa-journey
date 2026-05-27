class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        ans=0
        maxleft,maxright=height[0],height[len(height)-1]
        while left<right:
            if height[left]<height[right]:
                if height[left]<maxleft:
                    ans+=(maxleft-height[left])
                    left+=1
                else:
                    maxleft=max(maxleft,height[left])
                    left+=1

            else:
                if height[right]<maxright:
                    ans+=(maxright-height[right])
                    right-=1
                else:
                    maxright=max(maxright,height[right])
                    right-=1  
        return ans      