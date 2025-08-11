# This solution works for 987 testcases out of 988, the remaining one exceeds the time limit, see SolutionB for a better solution
class SolutionA(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s)==1:
            return 1

        present=[]
        totalMax= 0
        currentMax= 0
        check= 0

        for c in range(len(s)):
            if s[c] not in present:
                present.append(s[c])
                currentMax+=1
            else:
                if currentMax>totalMax:
                    totalMax=currentMax
               
                x=len(present)-1
                while x>=0:
                    if present[x]==s[c]:
                        check=x
                        break
                    x-=1

                if check==c-1:
                    currentMax=0
                else:
                    currentMax=c-(check+1)

                y=0
                present[:(check+1)]= [True] * (check+1)


                present.append(s[c])
                currentMax+=1
        
        if currentMax>totalMax:
            totalMax=currentMax
        return totalMax
