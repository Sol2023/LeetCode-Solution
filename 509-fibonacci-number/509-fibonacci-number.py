class Solution:
    def fib(self, n: int) -> int:
        lastTwo = [0,1]
        count =2
        while count <=n:
            nextNum = lastTwo[0] + lastTwo[1]
            lastTwo[0] = lastTwo[1]
            lastTwo[1] = nextNum
            count+=1
        return lastTwo[1] if n>0 else lastTwo[0]
    
        
        
        