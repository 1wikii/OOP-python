import csv

class item:

    discount  = 0.8
    total = []

    def __init__(self, name: str, price: float, quan=0):   # quan=0 mean we can empty quan while calling this class
        											       # name: str mean parameter only take string input
        
        # Checking eror with assert
        assert price >= 0, f"price {price} is not valid!"
        assert quan >= 0, f"quantity {quan} is not valid!"
        
        # Assign to self
        print(f"Product name : {name}")              
        self.name = name
        self.price = price
        self.quan = quan

        # Action to execute, store all data
        item.total.append(self)

    def calculate_total(self):
        self.total = self.price*self.quan
        print(self.total)

    def Discount(self):
       self.price = self.price * item.discount
       print(self.price)

    @classmethod                   # class method mean this code on scope class (no need parameter)
    def from_csv(cls):
        with open("CSV.csv","r") as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for i in items:
            item(
                name = i.get('name'),
                price = int(i.get('price')),
                quan = i.get('quantity'),
            )

        print(f"Dis = {cls.discount}")         # this is can access discount cause this def on scope class

    @staticmethod       # static method need parameter, on scope class
    def is_integer(num):
        if num % 1 == 0:
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quan})"


# Inherit or child class from item
class HP(item):

    hp_total = []
    def __init__(self, name: str, price: float, quan=0,broken=0):
        
        # super func to have access to all attribute from parent
        super().__init__(
            name, price, quan
        )

        # Checking eror with assert
        assert price >= 0, f"price {price} is not valid!"
        assert quan >= 0, f"quantity {quan} is not valid!"
        
        # Assign to self
        self.broken = broken

        # Execute action, store only child HP
        self.hp_total.append(self)


# a = HP("android",100,10)
# b = item("pc",20,1)


