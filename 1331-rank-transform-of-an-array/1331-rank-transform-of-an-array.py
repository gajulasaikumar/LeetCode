class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        n=(arr)
        arr=sorted(set(arr))
        d={}
        l=[]
        for i in range(len(arr)):
            d[arr[i]]=i+1
        print(n)
        for i in n:
            l.append(d[i])
        return l
                
            