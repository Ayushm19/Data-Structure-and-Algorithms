class Solution(object):
    def checkSubarraySum(self, nums, k):
        rem_map = {0 : -1}
        prefix_sum = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]

            remainder = prefix_sum % k
            if remainder in rem_map :
                if i - rem_map[remainder] >=2 :
                    return True
            else:
                rem_map[remainder] = i

        return False
        