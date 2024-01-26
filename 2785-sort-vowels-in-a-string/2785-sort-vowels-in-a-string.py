class Solution:
    def sortVowels(self, s: str) -> str:
        l=[]
        for i in s:
            if i in "aeiouAEIOU":
                l.append([ord(i),i])
        p=[]
        l.sort(reverse=True)
        for j in l:
            p.append(j[1])
        k=""
        for i in s:
            if i in "aeiouAEIOU":
                k=k+p.pop()
            else:
                k=k+i
        return k        
        