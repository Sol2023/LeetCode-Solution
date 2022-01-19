class Solution:
    def fib(self, n: int) -> int:
        memorize = {0:0,1:1}
        return self.getNFib(n, memorize)
    
    def getNFib(self, n, memorize) :
        if n in memorize:
            return memorize[n]
        else:
            memorize[n]=self.getNFib(n-1, memorize) + self.getNFib(n-2, memorize)
            return memorize[n]
    
        
        
        