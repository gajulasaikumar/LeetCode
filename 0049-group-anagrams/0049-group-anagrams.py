class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l=[]
        for i in strs:
            l.append("".join(sorted(i)))
        d={}
        for i in range(len(l)):
            if l[i] not in d:
                d[l[i]]=[strs[i]]
            else:
                d[l[i]]+=[strs[i]]
        return list(d.values())