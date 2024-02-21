class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            m=i
            for j in range(i+1,len(nums)):
                if nums[j]<nums[m]:
                    m=j
            t=nums[m]
            nums[m]=nums[i]
            nums[i]=t
            #nums[m],nums[i]=nums[i],nums[m]
        print(nums)
        l=[]
        for i in range(len(nums)):
            if target==nums[i]:
                l.append(i)
        return l