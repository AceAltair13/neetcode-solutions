class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        i, j = 0, 0
        _set = set()
        max_length = 1

        while j < len(s):
            if s[j] in _set:
                while s[j] in _set:
                    _set.remove(s[i])
                    i += 1
            else:
                _set.add(s[j])
                max_length = max(max_length, j - i + 1)
                j += 1

        return max_length
