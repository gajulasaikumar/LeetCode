class Solution:
    def canConstruct(self, ransomNote: str,magazine: str) -> bool:
        r=list(ransomNote)
        m=list(magazine)
        for i in r:
            if i in m:
                m.remove(i)
            else:
                return False
        return True


