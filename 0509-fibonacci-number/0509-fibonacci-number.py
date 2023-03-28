#memo = [-1]*31
class Solution:
    
    def fib(self, n: int) -> int:
        #recursive dp 
        #base cases
        #if n == 0: 
        #    return 0
        #if n == 1:
        #    return 1
        
        #if memo[n] != -1:
        #    return memo[n]
        
        #memo[n] = self.fib(n-1) + self.fib(n-2)
        #return memo[n]
        if n == 0:
            return 0
        if n == 2 or n == 1:
            return 1
        #iterative dp 
        dp = [0]*(n+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
        