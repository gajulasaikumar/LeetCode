class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        s=0
        m=0
        for i in gain:
            s=s+i
            if s>m:
                m=s
            
        return m