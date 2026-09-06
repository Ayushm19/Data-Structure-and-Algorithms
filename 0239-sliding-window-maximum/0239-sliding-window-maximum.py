class Solution(object):
   def maxSlidingWindow(self, nums, k):
    res = []
    deque_ = deque()

    for right in range(len(nums)):

        # Remove indices outside the current window
        while deque_ and deque_[0] <= right - k:
            deque_.popleft()

        # Remove smaller elements from the back
        while deque_ and nums[deque_[-1]] < nums[right]:
            deque_.pop()

        deque_.append(right)

        # Window has reached size k
        if right >= k - 1:
            res.append(nums[deque_[0]])

    return res
        