class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter

        i = 0
        j = len(s1) - 1
        check = Counter(s1)

        while j < len(s2):
            if Counter(s2[i : j + 1]) == check:
                return True
            i += 1
            j += 1

        return False
