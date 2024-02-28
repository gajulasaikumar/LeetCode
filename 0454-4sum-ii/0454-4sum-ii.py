class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
 
        c=0
        d=defaultdict(int)
        for i in nums1:
            for j in nums2:
                d[i+j]+=1
        for k in nums3:
            for l in nums4:
                if d[-1*(k+l)]!=0:
                    c+=d[-1*(k+l)]
        return c