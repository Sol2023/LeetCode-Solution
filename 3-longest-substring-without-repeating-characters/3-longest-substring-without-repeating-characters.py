class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = []
        maxL=0
        
        for char in s:
            if char not in substring:
                substring.append(char)
            else:
                for i, c in enumerate(substring):
                    if c==char:
                        substring = substring[i+1:]
                        substring.append(char)
       
            maxL = max(maxL, len(substring))
        return maxL