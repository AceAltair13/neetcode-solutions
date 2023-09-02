class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        from itertools import product

        ret = []

        def check_valid(strs):
            stack = []
            for p in strs:
                if stack:
                    if p == ")" and stack[-1] == "(":
                        stack.pop()
                        continue
                stack.append(p)
            return not stack

        for x in product(["(", ")"], repeat=2 * n):
            if check_valid(x):
                ret.append("".join(x))

        return ret
