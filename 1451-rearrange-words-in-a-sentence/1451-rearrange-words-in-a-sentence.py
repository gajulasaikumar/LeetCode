class Solution:
    def arrangeWords(self, text: str) -> str:
        d={}
        p=[]
        text=text.split(" ")
        for i in text:
            if i.lower() not in d:
                d[i.lower()]=len(i) 
        for i in text:
            p.append([len(i),i])
        m=max(list(d.values()))
        x=[ [] for i in range(m+1)]
        for k in p:
            x[k[0]].append(k[1])
        l=[]
        for i in x:
            l=l+i
        return " ".join(l).capitalize()