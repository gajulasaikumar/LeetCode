class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        c=0
        for i in range(len(strs[0])):
            s=""
            for j in range(len(strs)):
                s=s+strs[j][i]
            if "".join(sorted(s))!=s:
                c=c+1
        return c
                