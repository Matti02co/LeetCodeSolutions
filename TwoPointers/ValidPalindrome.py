"""
First solution reversing the string and cleaning it. O(n) Time and O(n) Space.
For a slightly better solution look at Solution2.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = re.sub(r'[^a-z0-9]', '', s.lower())
        return clean == clean[::-1]



"""
The second solution involves two pointers and allow us to reach O(1) Space. (still O(n) Time)
"""

"""
What did I learn? Two pointers approach and ord(n: int)
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l<r and not self.isAlphanumeric(s[l]):
                l+=1
            while l<r and not self.isAlphanumeric(s[r]):
                r-=1
            if s[l].lower() != s[r].lower():
                return False
            
            l+=1
            r-=1
        
        return True


    def isAlphanumeric(self, c):
        return ((ord('A')<=ord(c) and ord(c)<=ord('Z')) or 
                (ord('a')<=ord(c) and ord(c)<=ord('z')) or 
                (ord('0')<=ord(c) and ord(c)<=ord('9')))
