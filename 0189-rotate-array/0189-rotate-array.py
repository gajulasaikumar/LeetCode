class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)<k:
            k=k%len(nums)
            nums[:]=nums[len(nums)-k:]+nums[:len(nums)-k]
        else:
            nums[:]=nums[len(nums)-k:]+nums[:len(nums)-k]
        