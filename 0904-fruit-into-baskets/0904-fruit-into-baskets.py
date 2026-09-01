class Solution(object):
    def totalFruit(self, fruits):
        from collections import defaultdict

        map = defaultdict(int)
        left,max_len = 0,0

        for right in range(len(fruits)):
            map[fruits[right]] += 1

            while len(map) > 2:
                map[fruits[left]] -=1
                if map[fruits[left]] == 0:
                    del map[fruits[left]]
                left += 1
            
            max_len = max(max_len, right-left+1)
        
        return max_len
        