class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_len = len(s)
        t_len = len(t)

        i, j = 0, 0
        chars, count = {}, {}
        have, need = 0, t_len
        _i, _j, _size = -1, -1, float("infinity")

        for x in t:
            chars[x] = chars.get(x, 0) + 1

        for j in range(s_len):
            if s[j] in chars:
                count[s[j]] = count.get(s[j], 0) + 1
                if count[s[j]] <= chars[s[j]]:
                    have += 1

            while have == need:
                if s[i] in chars:
                    if j - i + 1 < _size:
                        _i, _j, _size = i, j, j - i + 1
                    count[s[i]] -= 1
                    if count[s[i]] < chars[s[i]]:
                        have -= 1
                i += 1

            j += 1

        return s[_i : _j + 1] if _size != float("infinity") else ""
