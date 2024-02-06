class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=""
        for i in s:
            if i.isalnum():
                s1+=i.lower()
        s=s1
        i=0
        j=len(s)-1
        while j>i:
            if s[i]!=s[j]:
                return False
            
            i+=1
            j-=1
        return True
            