class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result=[]
        startRow, endRow=0, len(matrix)-1
        startCol, endCol=0, len(matrix[0])-1
        
        while startRow <=endRow and startCol <= endCol:
            for col in range(startCol, endCol+1):
                result.append(matrix[startRow][col])
            startRow+=1
                
            for row in range(startRow, endRow+1):
                result.append(matrix[row][endCol])
            endCol-=1
            
            if startRow <= endRow:
                for col in reversed(range(startCol, endCol+1)):
                    result.append(matrix[endRow][col])
                endRow-=1
            
            if startCol <= endCol:
                for row in reversed(range(startRow, endRow+1)):
                    result.append(matrix[row][startCol])
                startCol+=1
        
        return result