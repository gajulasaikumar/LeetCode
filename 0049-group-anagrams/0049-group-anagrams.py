class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        for i in strs:
            x=[0]*26
            for j in i:
                x[ord(j)-ord("a")]+=1
                
            d[tuple(x)].append(i)
        return list(d.values())