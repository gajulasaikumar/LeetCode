class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(k):
            m=max(gifts)
            j=gifts.index(m)
            gifts[j]=int(m**(0.5))
        return sum(gifts)
            