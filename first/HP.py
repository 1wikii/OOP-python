from item import *

# Inherit or child class from item
class HP(item):

    # Example polymorphisme
    hp_total = []
    
    def __init__(self, name: str, price: float, quantity=0,broken=0):
        
        # super func to have access to all attribute from parent
        super().__init__(
            name, price, quantity
        )

        # Checking eror with assert
        assert price >= 0, f"price {price} is not valid!"
        assert quantity >= 0, f"quantity {quantity} is not valid!"
        
        # Assign to self
        self.broken = broken

        # Execute action, store only child HP
        self.hp_total.append(self)


# Inheritance principle
# buy = HP("IOS", 300, 2)
# buy.Discount()
# print(buy.price)