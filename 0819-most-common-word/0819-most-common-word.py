class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        d={}
        s=""
        for i in "!?',;.":
            paragraph=paragraph.replace(i," ")
        print(paragraph)
        x=paragraph.split(" ")
        for i in x:
            i=i.lower()
            if i not in banned and i!="":
                d[i]=1+d.get(i,0)
        print(d)
        m=max(d.values())
        for i in d:
            if d[i]==m:
                return i
            