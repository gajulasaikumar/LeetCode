class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        m=-1
        while j>i:
            l=(j-i)*min(height[i],height[j])
            print(l)
            m=max(m,l)
            if height[i]<height[j]:
                i=i+1
            else:
                j=j-1
        return m