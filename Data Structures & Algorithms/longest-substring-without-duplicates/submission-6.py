class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp=set()
        res=start=0
        for i in range(len(s)):
            while s[i] in mp:
                mp.remove(s[start])
                start+=1
            mp.add(s[i])
            res=max(res,i-start+1)
        return res

