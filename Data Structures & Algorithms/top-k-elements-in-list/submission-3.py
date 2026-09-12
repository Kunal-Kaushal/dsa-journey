class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mpp = Counter(nums)
        res = [key for key,freq in mpp.most_common(k)]
        return res