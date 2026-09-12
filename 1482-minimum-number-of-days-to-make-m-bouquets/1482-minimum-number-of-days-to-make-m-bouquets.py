class Solution(object):
    def minDays(self, bloomDay, m, k):
        n = len(bloomDay)
        if m*k > n:
            return -1
        
        low,high = min(bloomDay), max(bloomDay)
        ans =-1

        while low<=high:
            mid = (low + high)/2
            if self.canMake(bloomDay,m,k,mid):
                ans = mid
                high = mid-1
            else:
                low = mid + 1
        return ans

    def canMake(self,bloomDay,m,k,days):
        count =0
        bouqet =0

        for bloom in bloomDay:
            if bloom <= days:
                count += 1
                if count == k:
                    bouqet +=1
                    count =0
            else :
                count = 0
        return bouqet >= m
        