class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a = [1]*len(nums)
        mul = 1
        for i in range(1, len(nums)):
            a[i] = a[i-1]*nums[i - 1]
        print(a)    
        for j in range(len(nums) - 2, -1, -1):
            mul *= nums[j+1]
            a[j] = a[j]* mul
        print(mul)
        return a