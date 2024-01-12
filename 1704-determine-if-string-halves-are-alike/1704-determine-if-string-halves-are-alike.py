class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set("aeiouAEIOU")
        l, r = 0, len(s)-1
        leftVowel, rightVowel = 0,0
        while l < r:
            if s[l] in vowels:
                leftVowel += 1
            if s[r] in vowels:
                rightVowel += 1
            l+=1
            r-=1
        return leftVowel == rightVowel