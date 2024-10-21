class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        zeros = len(nums1)-m
        if not zeros:
            return
        if len(nums1)==1:
            nums1[0]=nums2[0]
            return
        p1, p2 = m-1, n-1
        while p1 >= 0 and not nums1[p1+p2+1]:
            maxNum = max(nums1[p1], nums2[p2])
            nums1[p1+p2+1] = maxNum
            if maxNum == nums1[p1]:
                nums1[p1] = 0
                p1 -= 1
            else:
                p2 -= 1
        while p2 >= 0:
            nums1[p2] = nums2[p2]
            p2 -= 1
            