class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nset, i = set(nums), 1
        while i in nset:
            i += 1
        return i
        