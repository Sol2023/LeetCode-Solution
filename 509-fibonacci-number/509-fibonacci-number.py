class Solution:
    def fib(self, n: int, memorize = {0:0,1:1}) -> int:
        if n in memorize:
            return memorize[n]
        else:
            memorize[n]=self.fib(n-1, memorize) + self.fib(n-2, memorize)
            return memorize[n]
        
        