class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        if len(nums1)< len(nums2):
            return self.intersect(nums2,nums1)
        
        dit ={}
        ans=[]
        
        for num in nums1:
            dit[num]=dit.get(num,0)+1
            
        for num in nums2:
            if num in dit and dit[num]>0:
                ans.append(num)
                dit[num]-=1
        
        return ans