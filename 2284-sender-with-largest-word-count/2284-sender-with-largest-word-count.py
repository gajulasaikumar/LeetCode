class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        d={}
        for i  in range(len(messages)):
            x=messages[i].split(" ")
            if senders[i] not in d:
                d[senders[i]]=len(x)
            else:
                d[senders[i]]+=len(x)
        m=max(d.values())
        l=[]
        for i in d:
            if d[i]==m:
                l.append(i)
        return sorted(l)[-1]