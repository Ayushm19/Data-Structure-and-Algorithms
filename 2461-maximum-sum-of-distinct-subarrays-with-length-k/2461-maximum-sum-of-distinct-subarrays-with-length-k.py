class Solution(object):
    def maximumSubarraySum(self, nums, k):
        n = len(nums)

        window_sum = sum(nums[:k])
        max_sum = 0

        count = {}

        # Count elements in first window
        for num in nums[:k]:
            count[num] = count.get(num, 0) + 1

        # First window is valid if all elements occur once
        if len(count) == k:
            max_sum = window_sum

        for i in range(k, n):

            window_sum += nums[i] - nums[i-k]

            # Remove outgoing element
            count[nums[i-k]] -= 1

            if count[nums[i-k]] == 0:
                del count[nums[i-k]]

            # Add incoming element
            count[nums[i]] = count.get(nums[i], 0) + 1

            # If number of unique elements == k
            if len(count) == k:
                max_sum = max(max_sum, window_sum)

        return max_sum