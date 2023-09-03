class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = list(map(str.lower, filter(str.isalnum, s)))
        n = len(s)

        for i in range(n // 2):
            if not s[i] == s[n - i - 1]:
                return False

        return True
