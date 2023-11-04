class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        _slow = 0

        while True:
            slow = nums[slow]
            _slow = nums[_slow]

            if slow == _slow:
                return slow
