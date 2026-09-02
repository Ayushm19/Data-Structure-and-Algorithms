class Solution(object):
    def maxSlidingWindow(self, nums, k):
        n = len(nums)
        res = [0] * (n-k+1)
        deque_ = deque()

        for right in range(n):
            #loop is removing indices that are outside the current sliding window
            while deque_ and deque_[0] <= right -k :
                deque_.popleft()
            #now we r checking if the num we r on is greater then deques num then del deque
            while deque_ and nums[deque_[-1]] < nums[right]:
                deque_.pop()
            
            deque_.append(right)
            #here we r checking if our sliding window has the target len or no 
            if right >= k-1 :
                res[right -k + 1] = nums[deque_[0]]
        return res
        