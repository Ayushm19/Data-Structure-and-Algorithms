class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1:
            return 0

        left, count = 0,0
        product = 1

        for right in range(len(nums)):
            product *= nums[right]

            while product >= k :
                product //= nums[left]
                left += 1
            
            count += right - left + 1 
        return count 