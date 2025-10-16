"""
Solution I wrote out of intuition. Time complexity O(nlogn) because of sorting, space O(n).
It could also be optimized, since I used useless variables.
For a better solution see Solution2.
"""

class Solution1:
    def longestConsecutive(self, nums: List[int]) -> int:
        temporaneo = []
        finale = []
        unici = set()
        disordinato = []
        

        for n in nums:
            unici.add(n)
        
        for n in unici:
            disordinato.append(n)
        
        ordinato = sorted(disordinato)

        

        for i in range(len(ordinato)):
            if len(temporaneo)==0:
                temporaneo.append(ordinato[i])
            elif(ordinato[i]-temporaneo[-1]==1):
                temporaneo.append(ordinato[i])
            else:
                if len(finale) < len(temporaneo):
                    finale = temporaneo
                temporaneo = [ordinato[i]]
        
        if len(finale) < len(temporaneo):
                    finale = temporaneo

        return len(finale)







"""
Both O(n)
"""

"""
What did I learn? You can create a set directly from a list. 
max to optimize and avoid condition checking.
"""

class Solution2:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxlen = 0
        insieme = set(nums)

        for n in insieme:
            if (n-1) not in insieme:
                lunghezza = 1
                while (n+lunghezza) in insieme:
                    lunghezza+=1
                maxlen = max(maxlen, lunghezza)
        return maxlen



