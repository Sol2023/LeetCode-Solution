class Solution:
    def reverseWords(self, s: str) -> str:
        newList=[]
        for string in s.split():
            newList.append(string[::-1])
        
        return ' '.join(newList)
    
        