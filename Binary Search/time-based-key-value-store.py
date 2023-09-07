class TimeMap:
    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = []
        self.timemap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        ret = ""
        data = self.timemap.get(key, [])

        i, j = 0, len(data) - 1

        while i <= j:
            mid = int((i + j) / 2)
            val, ts = data[mid]

            if ts <= timestamp:
                ret = val
                i = mid + 1
            else:
                j = mid - 1

        return ret


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
