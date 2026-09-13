class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sum=0
        res=[]
        curr=[]
        def backtrack(index):
            nonlocal sum
            if sum == target:
                res.append(curr.copy())
                return 
            if index==len(nums) or sum>target:
                return
            curr.append(nums[index])
            sum+=nums[index]
            backtrack(index)
            curr.pop()
            sum-=nums[index]
            backtrack(index+1)
        backtrack(0)
        return res

                