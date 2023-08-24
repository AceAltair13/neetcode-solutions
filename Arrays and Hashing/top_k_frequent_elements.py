class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        common_list = Counter(nums).most_common(k)
        ret = []
        for x in common_list:
            ret.append(x[0])
        return ret