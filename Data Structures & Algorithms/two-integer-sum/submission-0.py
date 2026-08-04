class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # only ONE pair i and j sum up to target
        # For loop tracking i and j approach is O(n^2)
        # target = nums[i] + nums[j], i != j
        # difference = target - nums[i]
        # Use a hash map to confirm i != j during second loop
        h = {}
        for i, num in enumerate(nums):
            h[num] = i
        
        for i, num in enumerate(nums):
            difference = target - num
            if difference in h and h[difference] != i:
                return [i, h[difference]]

