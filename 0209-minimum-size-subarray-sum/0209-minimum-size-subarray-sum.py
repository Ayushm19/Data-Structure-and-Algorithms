class Solution(object):
    def minSubArrayLen(self, target, nums):
        left , sum = 0,0
        min_len = float('inf')

        for right in range(len(nums)):
            sum += nums[right]

            while sum >= target:
                min_len = min(min_len, right - left + 1)

                sum -= nums[left]
                left +=1

        return 0 if min_len == float('inf') else min_len
        