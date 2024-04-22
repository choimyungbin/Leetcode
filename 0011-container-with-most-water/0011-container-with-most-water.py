class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        biggest = 0
        while l < r:
            volume = (r-l)*min(height[l],height[r])
            biggest = max(biggest, volume)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return biggest