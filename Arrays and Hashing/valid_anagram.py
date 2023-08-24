class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        s = Counter(s)
        t = Counter(t)
        return s == t