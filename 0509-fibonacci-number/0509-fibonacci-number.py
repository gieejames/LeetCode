memo = [-1]*31
class Solution:
    
    def fib(self, n: int) -> int:
        #recursive dp 
        #base cases
        if n == 0: 
            return 0
        if n == 1:
            return 1
        
        if memo[n] != -1:
            return memo[n]
        
        memo[n] = self.fib(n-1) + self.fib(n-2)
        return memo[n]
        
        #iterative dp 