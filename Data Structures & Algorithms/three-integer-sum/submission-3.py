class Solution:
    def helper(self,index, nums,res):
        i =index+1
        j=len(nums)-1
        while(i<j):
            sum = nums[i]+nums[j]+nums[index]
            if sum<0:
                i+=1
            elif sum>0:
                j-=1
            else:
                res.append([nums[index],nums[i],nums[j]])
                i+=1
                while i<j and nums[i]==nums[i-1]:
                    i+=1
                j-=1
                while i<j and nums[j]==nums[j+1]:
                    j-=1
        return res
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        if nums[0]>0:
            return []
        res=[]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            res = self.helper(i,nums,res)
        return res