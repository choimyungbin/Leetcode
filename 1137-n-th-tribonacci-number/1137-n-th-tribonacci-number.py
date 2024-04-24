class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0: return 0
        if n==1 or n==2: return 1
        tri = [0]*(n+1)
        tri[1] = 1
        tri[2] = 1
        for i in range(3, n+1):
            tri[i] = tri[i-1]+tri[i-2]+tri[i-3]
        return tri[n]
        