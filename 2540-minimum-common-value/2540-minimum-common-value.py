class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        m=float("inf")
        d={}
        for i in list(set(nums1))+list(set(nums2)):
            d[i]=1+d.get(i,0)
        for i in d:
            if d[i]>=2:
                m=min(i,m)
        if m==float("inf"):
            return -1
        return m