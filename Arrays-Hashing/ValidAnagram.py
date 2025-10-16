"""
This solution runs in O(nlogn + mlogm), (space and time complexity really depend on the sorting algorithm)
"""

"""
What did I learn? sorting also works for chars.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s)==sorted(t)