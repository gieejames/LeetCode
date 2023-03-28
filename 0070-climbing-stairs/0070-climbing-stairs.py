class Solution:
    def climbStairs(self, n: int) -> int:
        #two ways to get to the nth stair -> either from n - 1  or n - 2
        #base case
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]