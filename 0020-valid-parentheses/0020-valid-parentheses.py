class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        mapping = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        for ch in s:
            if ch in mapping:
                if not st or st.pop() != mapping[ch]:
                    return False
            else:
                st.append(ch)
        
        return len(st)==0