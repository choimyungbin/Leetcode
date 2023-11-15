class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        if arr[0] != 1:
            arr[0] = 1
        before = 1
        for i,n in enumerate(arr):
            if (n - before) > 1:
                arr[i] = before + 1
            before = arr[i]
        return arr[-1]