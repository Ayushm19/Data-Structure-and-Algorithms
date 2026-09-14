class Solution:
    def splitArray(self, nums, k):
        low, high = max(nums), sum(nums)
        ans = high

        while low <= high:
            mid = (low + high) // 2

            if self.canSplit(nums, k, mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

    def canSplit(self, nums, k, maxSum):
        count = 1
        currSum = 0

        for num in nums:
            if currSum + num <= maxSum:
                currSum += num
            else:
                count += 1
                currSum = num

        return count <= k
        