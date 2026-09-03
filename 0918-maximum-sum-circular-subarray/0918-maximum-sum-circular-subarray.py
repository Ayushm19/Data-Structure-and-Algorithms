class Solution(object):
    def kadane(self, nums):
        maxSum = nums[0]
        currSum = 0

        for num in nums:
            currSum += num
            maxSum = max(maxSum, currSum)

            if currSum < 0:
                currSum = 0
        return maxSum


    def maxSubarraySumCircular(self, nums):
        #normal subarray sum 
        normSubmax = self.kadane(nums)

        if normSubmax < 0:
            return normSubmax
        
        totalSum = sum(nums)
        for i in range(len(nums)):
            nums[i] *= -1
        
        #now max subarray of fliped = minimum of original
        maxFlipped = self.kadane(nums)

        circularMax = totalSum + maxFlipped

        return max(normSubmax, circularMax)
        
        