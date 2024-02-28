class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l=set()
        arr=nums
        arr.sort()
        n=len(arr)
        for i in range(n-1):
            x=i
            y=i+1
            d={}
            while y<n:
                s=-1*(arr[i]+arr[y])
                if s in d:
                    z=(arr[i],arr[y],d[s])
                    l.add(z)
                else:
                    d[arr[y]]=arr[y]
                                 
                y+=1
        return l