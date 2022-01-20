class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product =1
        sums= 0
        
        while n > 0:
            m = n%10
            product*=m
            sums+=m
            n= int(n/10)
        return product-sums
        