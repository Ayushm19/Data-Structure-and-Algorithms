class Solution(object):
    def moveZeroes(self, nums):
        left = 0
        n = len(nums)

        for right in range(n):
            if nums[right] :
                nums[left],nums[right] = nums[right],nums[left]
                left+=1
        