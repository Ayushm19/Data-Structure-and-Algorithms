class Solution(object):
    def maxProduct(self, nums):
        prefix, suffix = 1,1
        ans = float('-inf')
        n = len(nums)

        for i in range(n):
            
            if prefix == 0:
                prefix =1
            if suffix == 0:
                suffix = 1

            prefix *= nums[i]
            suffix *= nums[n-1-i]

            ans = max(prefix,suffix,ans)
        return ans
        