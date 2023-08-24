class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for x in strs:
            _key = tuple(sorted(list(x)))
            if _key not in groups:
                groups[_key] = [x]
            else:
                groups[_key].append(x)
        return list(groups.values())
