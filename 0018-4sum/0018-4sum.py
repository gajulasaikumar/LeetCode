class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        l=set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                k=j+1
                c=len(nums)-1
                while c>k:
                    s=nums[i]+nums[j]+nums[k]+nums[c]
                    if target>s:
                        k+=1
                    elif s>target:
                        c-=1
                    else:
                        l.add((nums[i],nums[j],nums[k],nums[c]))
                        c-=1
                        k+=1
        return l