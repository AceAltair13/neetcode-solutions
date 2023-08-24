class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0

        for x in nums:
            # check for start of sequence
            if not x - 1 in nums:
                _longest = 1
                while x + _longest in nums:
                    _longest += 1
                longest = max(_longest, longest)

        return longest
