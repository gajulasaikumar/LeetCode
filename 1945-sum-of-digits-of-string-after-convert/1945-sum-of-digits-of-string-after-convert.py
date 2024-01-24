class Solution:
    def getLucky(self, s: str, k: int) -> int:
        st=""
        for i in s:
            st=st+str(ord(i)-96)
        print(st)
        for j in range(k):
            su=0
            for k1 in st:
                su=su+int(k1)
            print(su)
            st=str(su)
        return (su)
            