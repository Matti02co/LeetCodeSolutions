"""
Time complexity O(nlogn), Space Complexity O(n).
"""

"""
What did I learn? Use of get to obtein a default value from a dictionary 
and the fact that sorting a dictionary, sorts it on the keys.
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurences = {}
        for n in nums:
            occurences[n]= occurences.get(n, 0) + 1
        
        unordered = []
        for n,c in occurences.items():
            unordered.append([c,n])
        ordered = sorted(unordered, reverse=True)
        
        res=[]
        for i in range(k):
            res.append(ordered[i][1])
        return res
