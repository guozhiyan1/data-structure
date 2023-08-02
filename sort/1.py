#[5,1,3,7,2]  时间复杂度nlogn，空间复杂度是n
class solutions:
    def Merge(self,arr):
        if len(arr)==1:
            return arr
        mid=len(arr)//2
        left=self.Merge(arr[0:mid])
        right=self.Merge(arr[mid:])
        return self.MergeSort(left,right)

    def MergeSort(self, left,right):
        l1=len(left)
        l2=len(right)
        a=[]
        i=j=0
        while i<l1 and j<l2:
            if left[i]<=right[j]:
                a.append(left[i])
                i+=1
            else:
                a.append(right[j])
                j+=1
        a=a+left[i:]+right[j:]
        return a
if __name__ == '__main__':
    a=[4,5,8,2,3,9,7,1]
    b=solutions()
    print(b.Merge(a))

