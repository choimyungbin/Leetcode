class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        original = x
        reverted = 0
        while x != 0:
            reverted = (reverted * 10) + (x % 10)
            x //= 10
        
        return original == reverted