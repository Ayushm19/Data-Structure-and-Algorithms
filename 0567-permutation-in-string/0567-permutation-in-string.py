class Solution(object):
    def checkInclusion(self, s1, s2):
        from collections import defaultdict

        mp = defaultdict(int)
        for ch in s1:
            mp[ch] += 1

        left =0

        for right in range(len(s2)):
            mp[s2[right]] -= 1

            if right - left + 1 > len(s1):
                mp[s2[left]] += 1
                left +=1
            
            if right - left + 1 == len(s1):
                if all(value == 0 for value in mp.values()):
                    return True
        
        return False
        