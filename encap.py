class Base: #Creating a base class
    def __init__(self):
        self._a = 2 #Creating a protected member
        self.__c = 3 #Creating private member

class Child(Base): #Creating a child class
    def __init__(self):

        Base.__init__(self)
        print("Calling protected member of base class:")
        print(self._a)

        Base.__init__(self)
        print("Calling private member of base class:")
        print(self.__c)

obj1 = Child()
obj2 = Base()

print(obj2.a) # Calling protected member
              # Outside class results in AttributeError

print(obj1.a)


