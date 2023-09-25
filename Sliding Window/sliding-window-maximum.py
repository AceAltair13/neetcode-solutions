class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque

        ret = []
        i = j = 0
        _deque = deque()

        while j < len(nums):
            while _deque and nums[_deque[-1]] < nums[j]:
                _deque.pop()
            _deque.append(j)

            if i > _deque[0]:
                _deque.popleft()

            if (j + 1) >= k:
                ret.append(nums[_deque[0]])
                i += 1

            j += 1

        return ret
