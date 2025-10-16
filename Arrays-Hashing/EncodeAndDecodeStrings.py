"""
Time complexity O(m), Space complexity O(m+n).
"""

"""
What did I learn? Perfectioned string manipulation.
"""

class Solution:

    def encode(self, strs: List[str]) -> str:
        lengths = []

        for s in strs:
            lengths.append("".join([str(len(s)), "#", s]))

        return  "".join(lengths)



    def decode(self, s: str) -> List[str]:
        
        stringhe = []
        
        i = 0

        while i < len(s):
            cur=""
            par=""
            while s[i] != "#":
                cur+=s[i]
                i+=1
            i+=1
            pos = i
            lun = int(cur)
            while i < pos+lun:
                par+=s[i]
                i+=1
            stringhe.append(par)
        return stringhe
