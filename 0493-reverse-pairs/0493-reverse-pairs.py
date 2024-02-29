class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge(arr,low,mid,high):
            i=low
            n=[]
            j=mid+1
            while i<=mid and j<=high:
                if arr[i]<=arr[j]:
                    n.append(arr[i])
                    i+=1
                else:
                    n.append(arr[j])
                    j+=1
            while i<=mid:
                n.append(arr[i])
                i+=1
            while j<=high:
                n.append(arr[j])
                j+=1
            for i in range(low,high+1):
                arr[i]=n[i-low]
        def countpairs(arr,low,mid,high):
            c=0
            j=mid+1
            for i in range(low,mid+1):
                while j<=high and arr[i]>(2*arr[j]):
                    j+=1
                c+=j-(mid+1)
            return c
        def mergesort(arr,low,high):
            c=0
            if low>=high:
                return c
            mid=(low+high)//2
            c+=mergesort(arr,low,mid)
            c+=mergesort(arr,mid+1,high)
            c+=countpairs(arr,low,mid,high)
            merge(arr,low,mid,high)
            return c
        x=mergesort(nums,0,len(nums)-1)
        return x