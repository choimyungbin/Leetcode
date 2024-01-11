class TimeMap:

    def __init__(self):
        self.hashMap = {} # key: [val,timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashMap:
            self.hashMap[key] = []
        self.hashMap[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        if not key in self.hashMap:
            return ""
        l, r = 0, len(self.hashMap[key])-1
        res = ""
        while l <= r:
            m = (l+r)//2
            if self.hashMap[key][m][1] <= timestamp:
                res = self.hashMap[key][m][0]
                l = m+1
            else:
                r = m-1
        return res
                

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)