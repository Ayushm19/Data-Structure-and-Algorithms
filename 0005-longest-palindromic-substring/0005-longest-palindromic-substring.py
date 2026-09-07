class Solution(object):
    def longestPalindrome(self, s):
        n = len(s)
        start,end = 0,0

        for i in range(n):
            len1 = self.expand_palindrome(s,i,i)
            len2 = self.expand_palindrome(s,i,i+1)

            length = max(len1,len2)

            if length > (end-start):
                start = i - (length-1)//2
                end = i + length//2

        return s[start:end+1]

    
    def expand_palindrome(self,s,l,r):
        while l>=0 and r<len(s) and s[l]==s[r]:
            l-=1
            r+=1
        return r-l-1


        