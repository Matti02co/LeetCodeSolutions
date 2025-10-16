"""
This solution has both time and space complexity of O(n).
"""

"""
What did I learn? Use of enumerate to obtein a numbered list and basic hashing.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}

        for i,n in enumerate(nums):
            hashmap[n]=i
        
        for i,n in enumerate(nums):
            complement=target-n
            if complement in hashmap and hashmap[complement]!=i:
                return [i, hashmap[complement]]