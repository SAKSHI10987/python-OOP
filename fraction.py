class Fraction:

    def __init__(self,x,y):
        self.num=x
        self.den=y

    def __str__(self):
        return '{}/{}'.format(self.num,self.den)  #whenever you put the object into the print function so python wants to know that how your object looks so bydefault it will to go str function of the class

    #how to add two objects of the class we have to write the add logic into our class to add teh objects otherwise it will give an error so whenever we have to add two objects of the same class then we use add magic method. whenever we write something like obj1+obj2 it automatically goes to add function of the class 
    def __add__(self, other):
        new_num=self.num*other.den+other.num*self.den
        new_den=self.den*other.den

        return '{}/{}'.format(new_num,new_den) 
    
    def __sub__(self, other):
        new_num=self.num*other.den-other.num*self.den
        new_den=self.den*other.den
        
        return '{}/{}'.format(new_num,new_den) 

    def __mul__(self, other):
            new_num=self.num*other.num
            new_den=self.den*other.den
            
            return '{}/{}'.format(new_num,new_den) 

    def __truediv__(self, other):
                new_num=self.num*other.den
                new_den=self.den*other.num
                
                return '{}/{}'.format(new_num,new_den) 
        





f1=Fraction(5,7)
f2=Fraction(2,4)
print(f1+f2)
print(f1-f2)
print(f1*f2)
print(f1/f2)