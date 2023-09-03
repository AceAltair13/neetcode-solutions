class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []
        n = len(nums)

        for i, x in enumerate(nums):
            if i > 0 and x == nums[i - 1]:
                continue

            j, k = i + 1, n - 1

            while j < k:
                _sum = nums[j] + nums[k] + x

                if _sum > 0:
                    k -= 1
                elif _sum < 0:
                    j += 1
                else:
                    ret.append([x, nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1

        return ret
