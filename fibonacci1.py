
class fibonacci:
    def __init__(self):
        self.val=[1]
        self.k=1;
    def grow(self):
        if(self.k==1):
            self.val.append(self.val[self.k-1])
        else:
            self.val.append(self.val[self.k-1]+self.val[self.k-2])
        self.k+=1
f1=fibonacci()
for i in range(30):
    f1.grow()
for i in range(f1.k):
    print(f1.val[i],end=' ')
    if((i+1)%5==0):
        print()
print("index=",f1.k)