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
            if s[c] not in present:    #if current char is not present, adds +1 to current length and append char to list
                present.append(s[c])
                currentMax+=1
            else:                         #else updates maximum if appropriate
                if currentMax>totalMax:
                    totalMax=currentMax
               
                x=len(present)-1
                while x>=0:
                    if present[x]==s[c]:
                        check=x               #finds repeated char index
                        break
                    x-=1

                if check==c-1:               #updates currentMax
                    currentMax=0
                else:
                    currentMax=c-(check+1)

                y=0
                present[:(check+1)]= [True] * (check+1)    #inserts an inert value in list for every element before repeated char


                present.append(s[c])    #adds element to list and update currentMax
                currentMax+=1
        
        if currentMax>totalMax:
            totalMax=currentMax
        return totalMax



"""
this solution works and uses a map to access O(1) the index of a char
19ms runtime and 13.41Mb of memory
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        present={}    #maps char -> index where it was last seen
        start=0    # start of window
        maxLength=0    

        for i in range(len(s)):
            if s[i] in present and present[s[i]]>=start:    #if char is in current window updates start
                start= present[s[i]] +1
            present[s[i]]=i                                 #inserts char in map 
            maxLength=max(maxLength, i-start+1)             #updates maxLength
        
        return maxLength

