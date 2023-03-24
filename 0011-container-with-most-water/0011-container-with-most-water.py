class Solution:
    def maxArea(self, H: List[int]) -> int:
        a, l, r = 0, 0, len(H) - 1
        while (l < r):
            if H[l] <= H[r]:
                res = H[l] * (r - l)
                l += 1
            else:
                res = H[r] * (r - l)
                r -= 1
            if res > a: 
                a = res
        return a
        