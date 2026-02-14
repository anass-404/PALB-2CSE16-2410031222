# Given an array arr[]. The task is to find the largest element and return it.

class Solution:
    def largestinarray(self, arr):
        max=0
        for i in arr:
            if max<i: max=i
        return max
obj=Solution()
arr = [11, 82, 79, 86, 100]
res=obj.largestinarray(arr)
print(res)
