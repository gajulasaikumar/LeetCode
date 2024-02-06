class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(numbers)):
            dif=target-numbers[i]
            if dif in d:
                return  [d[dif]+1,i+1]
            d[numbers[i]]=i
        print(d)
        