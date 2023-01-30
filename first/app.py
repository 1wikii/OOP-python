class item:
    def __init__(self, name: str, price: float, quan=0):   # quan=0 mean we can empty quan while calling this class
        												   # name: str mean parameter only take string input
        #checking eror with assert
        assert price >= 0, f"price {price} is not valid!"
        assert quan >= 0, f"quantity {quan} is not valid!"
        
        
        #assign to self object
        print(f"Name of product : {name}")              
        self.name = name
        self.price = price
        self.quan = quan

    def calculate_total(self):
        return self.price*self.quan


#Main
x = item("android",1000,10)

y = item("pc",2000,10)

print("price = ",end="")
print(x.calculate_total())
