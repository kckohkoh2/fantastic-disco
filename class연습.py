class contact:
    def __init__(self,name,age,gender,height,weight):
        self.name=name
        self.age=age 
        self.gender=gender
        self.height=height
        self.weight=weight
    def printout(self):
        print("%s: %d세 %s"%(self.name,self.age,self.gender))
    def bmi(self):
        height_meter=self.height/100
        bmi_val=self.weight/(height_meter**2)
        return bmi_val
p1=contact('Koh',62,'남',163.5,68.8)
p2=contact('Kim',52,'여',158.5,58.8)
p3=contact('cho',58,'남',178.5,78.5)
d={p1.name:p1}
d[p2.name]=p2
d[p3.name]=p3
for key in d:
    d[key].printout()

