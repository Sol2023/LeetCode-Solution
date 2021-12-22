class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans=[[1]]
        for i in range(1,rowIndex+1):
            ans.append(list(map(lambda x,y:x+y, ans[-1]+[0], [0]+ ans[-1])))
        
        return ans[-1]
        