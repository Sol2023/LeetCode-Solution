class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sidx=0
        tidx=0
        while sidx<len(s) and tidx <len(t):
            if t[tidx]==s[sidx]:
                sidx+=1
            tidx+=1
        return sidx==len(s)
        