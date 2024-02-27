class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        l=0
        p=[pref[0]]
        for i in range(1,len(pref)):
            l=pref[i]^pref[i-1]
            p.append(l)
        return p