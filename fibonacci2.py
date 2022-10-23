
class fibonacci2:
    def __init__(self):
        self.val1=0
        self.k=0
    def grow(self):
        if(self.k==0):
            self.val=1
        else:
            self.val=self.val1+self.val2
        self.val2=self.val1
        self.val1=self.val
        self.k+=1
        return self.val
f2=fibonacci2()
for i in range(30):
    print(f2.grow(),end=' ')
    if((i+1)%5==0):
        print()
print("index=",f2.k)