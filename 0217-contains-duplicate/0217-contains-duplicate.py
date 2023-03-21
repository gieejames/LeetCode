class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        
        #SOL 1 -> sort and for loop
        #nums.sort()
        #for i in range(len(nums) - 1):
        #    if nums[i] == nums[i+1]:
        #        return True
        #return False

        #SOL 2 -> set의 특징 활용
        return (len(set(nums)) != len(nums))
        