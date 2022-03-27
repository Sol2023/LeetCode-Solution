class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength=0
        mp={}
        left=0
        for right, char in enumerate(s):
            if char in mp:
                left=max(mp[char], left)
            
            maxLength = max(maxLength, right-left+1)
            mp[char]=right+1
        
        return maxLength
        
        
#         substring = []
#         maxL=0
        
#         for char in s:
#             if char not in substring:
#                 substring.append(char)
#             else:
#                 for i, c in enumerate(substring):
#                     if c==char:
#                         substring = substring[i+1:]
#                         substring.append(char)
       
#             maxL = max(maxL, len(substring))
#         return maxL


    