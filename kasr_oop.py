class fraction:
    def __init__(self, sorat, makhraj):
        self.s = sorat
        self.m = makhraj

    
    
    def SUM(self, a):
        result = fraction(None, None)
        result.s= self.sorat + a.sorat
        result.m = self.makhraj*self.a
        return result

    def Sub(self, a):
        result = fraction(None, None)
        self.s = self.sorat + a.sorat
        result.m = self.makhraj - a.makhraj
        return result

    def Mul(self, a):
        result = fraction(None, None)
        result.s = self.sorat * a.sorat
        result.m = self.makhraj* a.makhraj

    def Div(self, a):
        result = fraction(None, None)
        result.s =self.sorat * a.makhraj
        result.m = self.makhraj * a.sorat
        return result
    
kasr1=(3,5)
kasr2=(6,8)
def show(self):
        print(f"Result is: {self.sorat}/{self.makhraj}")
sum=kasr1.sum(kasr2)
print (sum)    

sum=kasr1.sub(kasr2)
print (sum)    

sum=kasr1.mul(kasr2)
print (sum)    

sum=kasr1.div(kasr2)
print (sum)    