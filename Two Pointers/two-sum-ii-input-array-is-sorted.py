class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ret = [0, 0]
        n = len(numbers)
        i = 0
        j = n - 1

        while i <= j:
            _sum = numbers[i] + numbers[j]

            if _sum == target:
                ret[0], ret[1] = i + 1, j + 1
                break

            elif _sum > target:
                j -= 1

            else:
                i += 1

        return ret
