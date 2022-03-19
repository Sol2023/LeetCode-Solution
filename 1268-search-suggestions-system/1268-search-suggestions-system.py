class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        ans=[]
        inputChar =''
        arrayLen = len(products)
        
        for char in searchWord:
            temp=[]
            inputChar+=char
            
            insertIdx = self.binarySearchIdx(products, inputChar)
            
            for wordIdx in range(insertIdx, min(arrayLen, insertIdx+3)):
                if products[wordIdx].startswith(inputChar):
                    temp.append(products[wordIdx])
            ans.append(temp)
        
        return ans
    
    def binarySearchIdx(self, array, target):
        left = 0
        right = len(array)
        
        while left < right:
            mid = left + (right-left)//2
            if array[mid]<target: left = mid+1
            else: right = mid
        
        return left