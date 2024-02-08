#%% inheritance tast
class Car :
    
    def __init__(self, brand, color, price):
        self.brand = brand
        self.color = color
        self.price = price
        
    def enginestart(self):
        print(self.brand + "열쇠로 시동 킴")
    def enginestop(self):
        print(self.brand + "열쇠로 시동 끔")
# =========================================================        
class SuperCar(Car) :
        
    def __init__(self, brand, color, price, mode):
        super().__init__(brand, color, price)
        self.mode = mode
        
    def openloof(self):
        print("지붕 열림")
        
    def closeloof(self):
        print("지붕 닫힘")

myCar = Car("hyundai", "Gray", 2500)
daddyCar = Car("Ferrari", "Red", 25000, "Sports")

# myCar.enginestart()
# daddyCar.enginestart()

# print(myCar.mode)
# print(daddyCar.mode)

daddyCar.openloof()

#%% (2) class var

class A:
    seq = 0
    
    def __init__(self) :
        A.seq += 1
        self.num = A.seq
        
    def test(self):
        A.seq = 10
        
obj1 =A()
obj2 =A()

print(obj1.num)
print(obj2.num)
obj1.test()

obj3 =A()
print(obj1.seq)
print(obj2.seq)
