class Solution:
    def isValid(self, s: str) -> bool:
        charmap = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for x in s:
            if stack:
                try:
                    if charmap[stack[-1]] == x:
                        stack.pop()
                        continue
                except:
                    pass
            stack.append(x)

        return not stack
