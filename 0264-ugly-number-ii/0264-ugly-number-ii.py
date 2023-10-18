class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # dp
        ugly_list = [0] * n
        ugly_list[0] = 1
        t2,t3,t5 = 0,0,0
        for i in range(1,n):
            # get the min number
            m2, m3, m5 = ugly_list[t2]*2, ugly_list[t3]*3, ugly_list[t5]*5
            minimum = min(m2, m3, m5)
            ugly_list[i] = minimum
            # increment idx only where we get the num
            # if 3 times because of duplicates (ex: 6 = 2*3 and 3*2)
            if minimum == m2:
                t2 += 1
            if minimum == m3:
                t3 += 1
            if minimum == m5:
                t5 += 1
        # print(ugly_list)
        return ugly_list[n-1]
        