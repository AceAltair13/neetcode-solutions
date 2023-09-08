class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ret = 0
        i = 0
        chars = {}
        max_freq = 0

        for j in range(len(s)):
            chars[s[j]] = 1 + chars.get(s[j], 0)
            max_freq = max(max_freq, chars[s[j]])

            while (j - i + 1) - max_freq > k:
                chars[s[i]] -= 1
                i += 1

            ret = max(ret, j - i + 1)

        return ret
