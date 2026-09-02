class Solution(object):
    def subarraysDivByK(self, nums, k):
        rem_count = {0 : 1}

        prefix_sum,count = 0,0

        for i in range(len(nums)):
            prefix_sum += nums[i]
            
            remainder = prefix_sum % k
            if remainder < 0:
                remainder += k
            
            if remainder in rem_count:
                count += rem_count[remainder]
            
            rem_count[remainder] = rem_count.get(remainder,0) + 1
        
        return count
        