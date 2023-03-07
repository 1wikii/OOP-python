class Product:
    def __init__(self,name="", manu="", amount=""):
        self.name = name
        self.manu = manu
        self.amount = amount

    def show(self):
        print(f"Product Name : {self.name}")
        print(f"Product Manufacturer : {self.manu}")
        print(f"Product Amount : {self.amount}")


class Service:
    def __init__(self, name="", provider=""):
        self.name = name
        self.provider = provider

    def show(self):
        print(f"Service Name : {self.name}")
        print(f"Service Provider : {self.provider}")


product_count = 0
service_count = 0


def validate_input():
    temp = input()
    if (temp == "exit()"):
        x = product_count + service_count
        print(f"Saved Item : {x}")
        print(f"Product : {product_count}")
        print(f"Service : {service_count}")
        return -1
    else:
        return temp

while True:
    x = validate_input()
    if (x == '1'):
        product = Product(input(),input(),input())
        product_count += 1
        print('Product saved!')
        product.show()
    elif (x == '2'):
        service = Service(input(),input())
        service_count += 1
        print('Service saved!')
        service.show()
    else:
        if x == -1:
            break
        else:
            print("Input is not valid!")
