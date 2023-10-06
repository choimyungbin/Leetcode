class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        k = len(nums)/3
        hashMap = {}
        res = []
        for n in nums:
            if n in hashMap:
                hashMap[n] += 1
            else:
                hashMap[n] = 1
        
        for key in hashMap.keys():
            if hashMap[key] > k:
                res.append(key)
        return res