#  Given an integer array arr[] and an integer k, your task is to find and return the kth smallest element in the given array. 

class Solution:
    def kthSmallest(self, arr, k):
        arr.sort()
        return arr[k-1]
obj=Solution()
arr=[11,32,64,22,78,92,47,22]
k=4
result=obj.kthSmallest(arr,k)
print(result)
