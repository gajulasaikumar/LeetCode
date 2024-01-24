class Solution:
    def digitSum(self, s: str, k: int) -> str:
        if len(s)<=k:
            return s
        s1=""
        for i in range(0,len(s),k):
                x=s[i:i+k]
                
                su=0
                for j in x:
                    su=su+int(j)
                s1=s1+str(su)
        print(s1)
        return self.digitSum(s1,k)
        
            
        