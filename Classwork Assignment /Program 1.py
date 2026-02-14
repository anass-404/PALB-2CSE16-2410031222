# You are given an array of integers arr[]. You have to reverse the given array. 
# Note: Modify the array in place. 

class Solution:
    def reverseArray(self , arc):
        # return arr(:: wrong)
        left,right=0,len(arr)-1
        while left < right:
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
            right-=1
        return arr
obj = Solution()
arr=[15,7,3,10,11,6]
result=obj.reverseArray(arr)
print(result)
