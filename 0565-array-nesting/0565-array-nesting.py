class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        p=set()
        m=0
        for i in range(len(nums)):
            x,z=set(),i
            c=0
            if z not in p:
                while True:
                    if nums[z] in x:
                        break
                    p.add(nums[z])
                    x.add(nums[z])
                    z=nums[z] #last index value
                    c+=1
            m=max(c,m)
        return m
                        
                    
                