class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        postfix = [1] * n
        answer = [1] * n

        for i in range(1, n):
            prefix[i] = nums[i-1] * prefix[i-1]
        for j in reversed(range(n-1)):
            postfix[j] = nums[j+1] * postfix[j+1]
        for k in range(n):
            answer[k] = prefix[k] * postfix[k]

        return answer