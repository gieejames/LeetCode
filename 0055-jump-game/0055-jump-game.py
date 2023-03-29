class Solution:
    def canJump(self, nums: List[int]) -> bool:
        a = 0
        for val in nums:
            if a < 0:
                return False
            a = max(a, val)
            a -= 1
        return True