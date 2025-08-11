"""
This solution works for 987 testcases out of 988, the remaining test exceeds the time limit, see SolutionB for a better solution
"""
class SolutionA(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s)==1:
            return 1

        present=[]    #characters in current substring
        totalMax= 0    #maximum substring length until now
        currentMax= 0    #current substring length
        check= 0    #index of repeated char

        for c in range(len(s)):
            if s[c] not in present:    #if current char is not present, add +1 to current length and append char to list
                present.append(s[c])
                currentMax+=1
            else:                         #else update maximum if appropriate
                if currentMax>totalMax:
                    totalMax=currentMax
               
                x=len(present)-1
                while x>=0:
                    if present[x]==s[c]:
                        check=x               #find repeated char index
                        break
                    x-=1

                if check==c-1:               #update currentMax
                    currentMax=0
                else:
                    currentMax=c-(check+1)

                y=0
                present[:(check+1)]= [True] * (check+1)    #insert an inert value in list for every element before repeated char


                present.append(s[c])    #add element to list and update currentMax
                currentMax+=1
        
        if currentMax>totalMax:
            totalMax=currentMax
        return totalMax



"""
this solution works and uses a map to access O(1) the index of a char
"""
class SolutionB(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return len(s)

        present = {}    # map char-> last seen index
        totalMax = 0    #max length
        start = 0     # window start

        for c in range(len(s)):
            if s[c] in present and present[s[c]] >= start:
                # update window start
                start = present[s[c]] + 1
            present[s[c]] = c                 #update index of char
            totalMax = max(totalMax, c - start + 1)    #calculate max length until now

        return totalMax

