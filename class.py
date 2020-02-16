#Create a Class

class myClass:
    x = 5

className = myClass()
print(className.x)


#Constractor Or __ini__

class parson:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("My Name : " + name)
        print("My Age : " + age)

p = parson('sohag','24')