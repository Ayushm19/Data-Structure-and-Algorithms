class Solution(object):
    def subarraySum(self, nums, k):
        prefix_sum = 0
        count = 0
        map = {0 : 1}

        for num in nums:
            prefix_sum += num

            if prefix_sum - k in map:
                count += map[prefix_sum-k]

            map[prefix_sum] = map.get(prefix_sum,0) + 1

        return count        