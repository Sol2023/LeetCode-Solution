

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [ [ 0 for i in range(n) ] for j in range(n) ]
        startRow, endRow=0, n-1
        startCol, endCol=0, n-1
        currentNum =0
        
        while startRow<= endRow and startCol <= endCol:
            for col in range(startCol, endCol+1):
                currentNum+=1
                matrix[startRow][col]=currentNum
            
            for row in range(startRow+1, endRow+1):
                currentNum+=1
                matrix[row][endRow]=currentNum
                
            for col in reversed(range(startCol, endCol)):
                currentNum+=1
                matrix[endRow][col]=currentNum
            
            for row in reversed(range(startRow+1, endRow)):
                currentNum+=1
                matrix[row][startCol]=currentNum
            
            startRow+=1
            endRow-=1
            startCol+=1
            endCol-=1
            
    
        return matrix

            
            
        