class Solution(object):
    def minSpeedOnTime(self, dist, hour):
        low, high = 1, 10**7
        ans = -1
        while low <= high:
            mid = low+(high-low)//2

            if self.canReach(dist,hour,mid):
                ans = mid
                high = mid - 1
            else:
                low = mid+1
        return ans 

    def canReach(self,dist,hour,speed):
        time = 0.0
        for i in range(len(dist)):
            t = dist[i] / float(speed)
            if i != len(dist) - 1:
                time += math.ceil(t)
            else:
                time += t
        return time <= hour