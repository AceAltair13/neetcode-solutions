class Solution:
    def trap(self, height: List[int]) -> int:
        i, j, = 0, len(height) - 1
        i_max, j_max = height[i], height[j]
        water = 0

        while i < j:

            if i_max < j_max:
                i += 1
                i_max = max(i_max, height[i])
                water += i_max - height[i]
            else:
                j -= 1
                j_max = max(j_max, height[j])
                water += j_max - height[j]

        return water