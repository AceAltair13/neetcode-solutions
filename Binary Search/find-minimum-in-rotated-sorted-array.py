class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1
        ret = nums[0]

        while i <= j:
            if nums[i] < nums[j]:
                ret = min(ret, nums[i])
                break

            mid = int((i + j) / 2)
            ret = min(ret, nums[mid])

            if nums[mid] >= nums[i]:
                i = mid + 1
            else:
                j = mid - 1

        return ret
