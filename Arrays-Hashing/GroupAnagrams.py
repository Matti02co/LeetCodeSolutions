"""
Time complexity O(m + nlogn), Space complexity O(m*n).
"""

"""
What did I learn? Use of defaultdict of list and the fact you have to "re-join" sorted string
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dictionary = defaultdict(list)
        for s in strs:
            dictionary["".join(sorted(s))].append(s)
        return list(dictionary.values())
