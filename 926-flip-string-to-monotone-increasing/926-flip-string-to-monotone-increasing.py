class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        one =0
        flip =0
        for i in range(len(s)):
            print(i, s[i], one, flip)
            if s[i]=='1':
                one+=1
            else:
                flip+=1
            flip = min(one, flip)
        return flip
        