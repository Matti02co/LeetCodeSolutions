"""
First solution obteined converting number to string, O(n) Time, O(1) Space.
Look at Solution2 to solve it without converting x to str.
"""

class Solution1(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]
    


"""
Solution reversing half of the nuber. O(n) Time and O(n) space
"""

"""
What did I learn? How can I use math to reverse a number
"""

class Solution2(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        rHalf = 0
        while x > rHalf:
            rHalf = rHalf * 10 + x % 10
            x //= 10
        
        return rHalf == x or rHalf // 10 == x