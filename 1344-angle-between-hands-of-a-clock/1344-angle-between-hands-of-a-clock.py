class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        m=minutes/12
        if hour!=12:
            t1=hour*5
        else:
            t1=0
        t2=t1+m
        t3=abs(minutes-t2)
        s=t3*6
        return (min(s,360-s))