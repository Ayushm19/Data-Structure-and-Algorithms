class Solution(object):
    def kadane(self,nums):
        maxSum = nums[0]
        currSum = 0

        for num in nums:
            currSum += num
            maxSum = max(maxSum, currSum)

            if currSum < 0:
                currSum =0
        return maxSum

    def maxAbsoluteSum(self, nums):
        
        # normal array max
        normalarrayMaxsum = self.kadane(nums)

        #flip the array
        for i in range(len(nums)):
            nums[i] *= -1

        flippedarrayMaxsum = self.kadane(nums)

        return max(normalarrayMaxsum, flippedarrayMaxsum)
        