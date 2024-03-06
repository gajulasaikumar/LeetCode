class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        def solve(arr):
            x=arr[0]**arr[1]
            return ((x%10)**arr[2] )% arr[3]
        l=[]
        for i in range(len(variables)):
            if solve(variables[i])==target:
                l.append(i)
        return l