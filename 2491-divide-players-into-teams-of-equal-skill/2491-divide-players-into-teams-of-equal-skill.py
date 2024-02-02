class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if len(skill)<=2:
            return skill[0]*skill[1]
        skill.sort()
        h=len(skill)-1
        l=0
        li=[]
        p=[]
        while h>l:
            li.append(skill[h]*skill[l])
            p.append(skill[h]+skill[l])
            h=h-1
            l=l+1
        if len(set(p))==1:
            return sum(li)
        return -1