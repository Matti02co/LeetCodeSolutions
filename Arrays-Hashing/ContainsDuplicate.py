"""
This solution runs in O(n).
"""

"""
What did I learn? Use of set.
"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        singoli = set()
        for n in nums:
            if n in singoli:
                return True
            singoli.add(n)
        return False
