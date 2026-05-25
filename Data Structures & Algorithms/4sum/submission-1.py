class Solution:
    def helper(self,index, nums,target,res,first_num,second_num):
        i =index+1
        j=len(nums)-1
        while(i<j):
            sum = nums[i]+nums[j]+second_num+first_num
            if sum<target:
                i+=1
            elif sum>target:
                j-=1
            else:
                res.append([first_num,nums[index],nums[i],nums[j]])
                i+=1
                while i<j and nums[i]==nums[i-1]:
                    i+=1
                j-=1
                while i<j and nums[j]==nums[j+1]:
                    j-=1
        return res
    def threeSum(self,index, nums, target,res,first_num) -> List[List[int]]:
        i = index+1
        for i in range(i,len(nums)):
            if i>index+1 and nums[i]==nums[i-1]:
                continue
            res = self.helper(i,nums,target,res,first_num,nums[i])
        return res
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            res = self.threeSum(i,nums,target,res,nums[i])
        return res