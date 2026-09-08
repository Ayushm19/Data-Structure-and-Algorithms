class Solution(object):
    def minWindow(self, s, t):
        from collections import defaultdict
        map = defaultdict(int)
        for c in t:
            map[c] += 1

        left =0
        ans = ""
        minLen = float('inf')
        count = len(t)

        for right in range(len(s)):
            ch = s[right]
            if ch in map:
                if map[ch] > 0:
                    count -=1
                map[ch] -=1

            while count == 0:
                if right-left+1 < minLen:
                    minLen = right-left+1
                    ans = s[left:right+1]
                
                leftch = s[left]
                if leftch in map :
                    map[leftch] += 1
                    if map[leftch] > 0 : count+=1
                
                left+=1
        return ans
        