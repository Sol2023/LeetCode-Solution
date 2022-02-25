class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split('.')
        version2 = version2.split('.')  
        
        l1 = len(version1)
        l2 = len(version2)
         
        for i in range(max(l1, l2)):
            n1 = int(version1[i]) if i<l1 else 0
            n2 = int(version2[i]) if i<l2 else 0
        
            if n1 !=n2:
                return 1 if n1>n2 else -1
        
        return 0