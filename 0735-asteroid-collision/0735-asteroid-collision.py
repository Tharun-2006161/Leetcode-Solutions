class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        a=asteroids
        st=[]
        for i in range(len(a)):
            if a[i]>=0:
                st.append(a[i])
            elif a[i]<0 and st and st[-1]>=0:
                while (st and st[-1]>0 and abs(a[i])>st[-1]):
                    st.pop()
                if st and abs(a[i]) == st[-1]:
                    st.pop()
                elif len(st)==0 or st[-1]<0:
                    st.append(a[i])         
            else:
                st.append(a[i])
        return st
