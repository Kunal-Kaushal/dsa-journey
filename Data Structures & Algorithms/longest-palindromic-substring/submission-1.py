class Solution:
    def longestPalindrome(self, s: str) -> str:
        index=0
        reslen=0
        def isPalindrome(l,r):
            nonlocal index,reslen
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1) > reslen:
                    index=l
                    reslen=r-l+1
                l-=1
                r+=1
        
        for i in range(len(s)):
            l,r = i,i
            isPalindrome(l,r)

            l,r=i,i+1
            isPalindrome(l,r)

        return s[index:index+reslen]