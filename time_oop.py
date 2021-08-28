class watch:
    def __init__(self,h,m,s,h1,m1,s1):
        self.h=h
        self.m=m
        self.s=s

        self.h1=h1
        self.m1=m1
        self.s1=s1

        

    def sum_time(self):
        result =()
        self.h= self.h + self.h1
        self.m=self.m+self.m1
        self.s=self.s+self.s1
        
        if result.s >=60:
            result.s-= 60
            result.m += 1

        if result.m >= 60:
            result.m -=60
            result.h +=1

        if result.h > 23 :
            result.h -= 24

        return result
    def sub_time(self):
        result =()
        self.h= self.h - self.h1
        self.m=self.m-self.m1
        self.s=self.s-self.s1
        if result.s < 0:
            result.m =- 1
            result.h =+ 60
        if result.m < 0:
            result.h -= 1
            result.m =+ 60
        return result

    def sec_to_hours(self):
        sec=int(input("enter second for convert to hours:"))
        result=()
        self.h= self.sec // 3600
        self.m = (self.sec % 3600) // 60
        self.s = (self.sec% 3600) % 60
        return result

    def hours_to_sec(self):
        second =(self.h*3600 +self.m*60 + self.s)
        return second

    def show(self):
        print(self.h, ":", self.m, ":", self.s)

t1 ={"h":3, "m":30, "s":45}
t2={"h":13, "m":46, "s":30}
t3= t1.sum_time(t2)
print(t3)

t4=t1.sub_timet(t2)
print (t4)

s_to_h=sec.sec_to_hours()
print (s_to_h)

h_to_s=t1.hours_to_sec()
print(h_to_s)