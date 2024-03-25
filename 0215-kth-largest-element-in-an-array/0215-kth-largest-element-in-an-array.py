class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        x=sorted(nums)[::-1]
        print(x)
        return x[k-1]