class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter
        for val in Counter(nums).values():
            if val > 1: return True