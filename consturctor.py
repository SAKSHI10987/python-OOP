#what is consturctor

# constructor is a method user does not have the control on the constructor function

#Any setting or functionality that you don't want the app user to control should be written inside the constructor.

#example to write configuration related code like (connecting my application with databse)

# In a class, one method can access other methods and attributes of the same object using `self`. We pass `self` as the first parameter of every instance method.

# `self` represents the current object. Therefore, using `self`, we can access other methods and attributes that belong to the current object inside the class.

# For example:

# ```python
# class Student:
 
#     def __init__(self, name):
#         self.name = name

#     def display(self):
#         print(self.name)
# ```

# Here, `self.name` refers to the `name` attribute of the current object.
# # 

class c:
    def __init__(self):
        self.pin=''
        self.balance=0
        print(id(self))

obj=c()
print(id(obj))

    
