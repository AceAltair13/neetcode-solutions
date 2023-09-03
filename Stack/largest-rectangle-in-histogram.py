class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        n = len(heights)

        for i in range(n):
            start = i
            h = heights[i]

            while stack and stack[-1][1] > h:
                ind, ht = stack.pop()
                max_area = max(max_area, ht * (i - ind))
                start = ind

            stack.append((start, h))

        for i, h in stack:
            max_area = max(max_area, h * (n - i))

        return max_area
