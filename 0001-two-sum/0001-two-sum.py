class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #key -> number, value -> index so that we can access index easily 
        d = {}
        for i,j in enumerate(nums):
            sub = target - j
            if sub in d: 
                return [d[sub], i]
            d[j] = i