class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        x=strs[0]
        y=strs[-1]
        s=""
        for i in range(min(len(x),len(y))):
            if x[i]==y[i]:
                s=s+x[i]
            else:
                break
        return s