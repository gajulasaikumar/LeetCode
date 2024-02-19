class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s=set()
        for i in emails:
            x=i.index("@")
            y=x
            if "+" in i:
                y=i.index("+")
            a=i[:y]
            a=a.replace(".","")
            n=a+i[x:]
            s.add(n)
        return len(s)