class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        for i in range(size):
            try:
                return [i, nums.index(target - nums[i], i + 1)]
            except:
                continue
