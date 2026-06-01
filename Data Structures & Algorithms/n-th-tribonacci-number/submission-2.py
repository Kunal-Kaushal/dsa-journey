class Solution:
    def tribonacci(self, n: int) -> int:
        T0,T1,T2=0,1,1
        if n<3:
            if n ==1 or n == 2:
                return T1
            else:
                return 0
        
        for i in range(3,n+1):
            temp1 = T1
            temp2 = T2
            T2=T0+T1+T2
            T1=temp2
            T0=temp1
        return T2
