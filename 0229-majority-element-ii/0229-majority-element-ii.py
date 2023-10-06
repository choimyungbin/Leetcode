class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        k = len(nums)//3
        hashMap = {}
        res = []
        # hashMap == Counter(nums)
        for n in nums:
            if n in hashMap:
                hashMap[n] += 1
            else:
                hashMap[n] = 1
        
        for key, item in hashMap.items():
            if item > k:
                res.append(key)
        return res
    