class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mpp={}
        for s in strs:
            ss=sorted(s)
            ss=''.join(ss)
            if ss not in mpp:
                mpp[ss]=[]
            mpp[ss].append(s)
        return list(mpp.values())
        
