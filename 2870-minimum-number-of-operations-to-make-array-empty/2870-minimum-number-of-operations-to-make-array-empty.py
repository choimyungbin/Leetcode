class Solution:
    def minOperations(self, nums: List[int]) -> int:
        hashMap = {}
        res = 0
        for n in nums:
            if n in hashMap.keys():
                hashMap[n] += 1
            else:
                hashMap[n] = 1
        
        for n in hashMap.keys():
            while hashMap[n] > 4:
                hashMap[n] -= 3
                res += 1
            if hashMap[n] == 4:
                hashMap[n] -= 4
                res += 2
            elif hashMap[n] == 3:
                hashMap[n] -= 3
                res += 1
            elif hashMap[n] == 2:
                hashMap[n] -= 2
                res += 1
            elif hashMap[n] == 1 or hashMap[n] == 0:
                return -1
            
        
        return res