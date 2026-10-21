class TimeMap:

    def __init__(self):
        self.dict = {} # hash map storing tuples

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dict:
            self.dict[key].append((timestamp, value)) # 
        else:
            self.dict[key] = [(timestamp, value)]



    def get(self, key: str, timestamp: int) -> str:
        # Key DNE
        if key not in self.dict:
            return ""
        
        values = self.dict[key] # finds all values associated with key

        # Do binary search to find largest timestep <= target timestep
        l, r = 0, len(values) - 1
        val = ""

        while l <= r:
            mid = (l + r) // 2
            if values[mid][0] <= timestamp:
                val = values[mid][1] # valid candidate
                l = mid + 1
            else:
                r = mid - 1 # target timestamp is smaller
        return val



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)