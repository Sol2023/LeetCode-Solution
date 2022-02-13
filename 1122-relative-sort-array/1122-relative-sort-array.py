class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dictRelative = {}
        restElement = []
        result=[]
        
        for num in arr2:
            dictRelative[num]=0
            
        for num in arr1:
            if num in dictRelative:
                dictRelative[num]+=1
            
            else:
                restElement.append(num)
            
        restElement.sort()
        
        for num in dictRelative:
            result.extend([num]*dictRelative[num])
        
        result.extend(restElement)
        
        return result
        