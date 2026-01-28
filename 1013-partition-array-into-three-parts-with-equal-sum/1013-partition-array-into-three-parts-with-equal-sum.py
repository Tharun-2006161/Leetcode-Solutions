class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total=sum(arr)
        if total%3!=0:
            return False
        else:
            target=total//3
            cs=0
            c=0
            for i in range(len(arr)):
                cs+=arr[i]
                if cs==target:
                    c+=1
                    cs=0
            if c>=3:
                return True
            else:
                return False