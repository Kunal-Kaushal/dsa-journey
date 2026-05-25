class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        streak = 0
        ans=0
        for num in nums:
            current = num
            if current-1 not in s:
                while current in s:
                    streak+=1
                    current = current+1
            ans=max(ans,streak)
            streak=0
        return ans
