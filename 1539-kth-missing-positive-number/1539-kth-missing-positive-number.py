class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left=0
        right= len(arr)
        while left < right:
            m=int((right+left)/2)
            if arr[m]-m-1<k:
                left=m+1
            else:
                right=m
        return left+k