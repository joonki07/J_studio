#%% (1) 
class A:
    data = 10
    
    def printdata(self):
        print(self.data)
    
    def intro():
        print("나는 A클래스 입니다")
        
obj1 = A()
obj2 = A()

obj1.data = 30
print(obj2.data)
print(obj1.data)



#%% (2) class test
class Car:
    brand = ""
    color = ""
    price = 0
    
    def __init__(self, brand, color, price):
        self.brand = brand
        self.color = color
        self.price = price
    
    def enginestart(self):
        print(self.brand + "시동 킴")
    def enginestop(self):
        print(self.brand + "시동 끔")
        
momCar = Car("Genesis", "Yellow", 4700)
daddyCar = Car("Hyundai")

momCar.enginestart()
daddyCar.enginestart()
print(momCar.color)      
  
# momCar = Car()
# daddyCar = Car()
# myCar = Car()

# momCar.brand = "Genesis"
# momCar.color = "Yellow"
# momCar.price = 4700

# daddyCar.brand = "Hyundai"
# daddyCar.color = "Black"

# print(momCar.brand)
# momCar.enginestart()
# daddyCar.enginestart()
