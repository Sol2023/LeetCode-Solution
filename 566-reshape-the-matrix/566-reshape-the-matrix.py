class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        res = []
        temp = []
        
        if len(mat)==0 or r*c != len(mat)*(len(mat[0])):
            return mat
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                temp.append(mat[i][j])
                
                if len(temp)==c:
                    res.append(temp)
                    temp=[]
        
        return res