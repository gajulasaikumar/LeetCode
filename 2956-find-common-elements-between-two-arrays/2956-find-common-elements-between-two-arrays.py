class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c=0
        c1=0
        for i in nums1:
            if i in nums2:
                c=c+1
        for j in nums2:
            if j in nums1:
                c1=c1+1
        return [c,c1]