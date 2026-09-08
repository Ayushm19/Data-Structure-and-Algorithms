class Solution(object):
    def lengthOfLongestSubstring(self, s):
        from collections import defaultdict
        mp = defaultdict(int)
        left = 0
        maxLen = 0

        for right in range(len(s)):
            mp[s[right]] += 1
            
            while mp[s[right]] > 1:
                mp[s[left]] -= 1
                left +=1

            maxLen = max(maxLen, right-left+1)
        
        return maxLen
        