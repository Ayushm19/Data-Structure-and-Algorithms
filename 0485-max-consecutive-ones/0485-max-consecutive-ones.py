class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        n = len(nums)
        max_count, current_count = 0,0

        for i in range(n):
            if nums[i] == 1:
                current_count += 1
            else:
                max_count = max(max_count, current_count)
                current_count = 0
        return max(max_count,current_count)

        