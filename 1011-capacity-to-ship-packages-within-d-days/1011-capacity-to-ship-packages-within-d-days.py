class Solution(object):
    def shipWithinDays(self, weights, days):
        low, high = max(weights), sum(weights)

        while low <= high:
            mid = low + (high-low)//2

            if self.canShip(weights,days,mid):
                ans = mid
                high = mid-1
            else:
                low = mid +1
        return ans

    def canShip(self,weights,days,cap):
        d = 1
        curr = 0

        for w in weights:
            if w + curr > cap:
                d += 1
                curr = w
            else:
                curr += w
        return d <= days
        