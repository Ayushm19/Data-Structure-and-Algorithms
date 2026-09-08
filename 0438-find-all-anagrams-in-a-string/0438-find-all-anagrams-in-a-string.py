class Solution(object):
    def findAnagrams(self, s, p):
        from collections import defaultdict
        res = []
        if len(s) < len(p):
            return res

        mp = defaultdict(int)
        for i in p:
            mp[i] +=1

        left = 0
        count = len(p)
        for right in range(len(s)):
            rightchar = s[right]
            rightvalue = mp[rightchar]
            if rightvalue > 0:
                count -=1
            mp[rightchar] = rightvalue - 1

            if right-left+1 > len(p):
                leftchar = s[left]
                leftvalue = mp[leftchar]
                if leftvalue >= 0:
                    count+=1
                mp[leftchar] = leftvalue+1
                left += 1
            
            if count == 0:
                res.append(left)
        
        return res
        