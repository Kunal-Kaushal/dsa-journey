class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pmul = nums[0]
        prefix=[1]
        for i in range(1,len(nums)):
            prefix.append(pmul)
            pmul*=nums[i]
        smul = nums[-1]
        suffix=[1]
        for i in range(len(nums)-2,-1,-1):
            suffix.append(smul)
            smul*=nums[i]
        suffix.reverse()
        ans=[]
        for i in range(len(nums)):
            ans.append(prefix[i]*suffix[i])
        return ans
        
        
