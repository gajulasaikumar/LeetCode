class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def checkarth(n):
            dif=n[1]-n[0]
            x=n[0]
            for i in n[1:]:
                if (i-x)!=dif:
                    return False
                x=i
            return True
        li=[]
        for i in range(len(l)):
            x=nums[l[i]:r[i]+1]
            x.sort()
            li.append(checkarth(x))
        return li