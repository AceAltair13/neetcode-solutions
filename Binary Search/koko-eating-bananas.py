class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        from math import ceil

        i = 1
        j = max(piles)
        k = 0
        n = len(piles)
        ret = j

        while i <= j:
            mid = int((i + j) / 2)
            _h = 0

            for x in piles:
                _h += ceil(x / mid)

            if _h <= h:
                ret = min(ret, mid)
                j = mid - 1
            else:
                i = mid + 1

        return ret
