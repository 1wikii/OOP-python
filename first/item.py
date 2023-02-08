import csv

class item:

    discount  = 0.2  # 20%
    total = []

    def __init__(self, name: str, price: float, quantity=0):   # quan=0 mean we can empty quan while calling this class
        											       # name: str mean parameter only take string input
        
        # Checking eror with assert
        assert price >= 0, f"price {price} is not valid!"
        assert quantity >= 0, f"quantity {quantity} is not valid!"
        
        # Assign to self
        print(f"Product name : {name}")     

        self.__name = name          # double underscore on name, mencegah attribute name tidak keluar scope kelas
        self.__price = price
        self.quantity = quantity

        # Action to execute, store all data
        item.total.append(self)

    def calculate_total(self):
        self.total = self.__price*self.quantity

    def Discount(self):
       self.__price = self.__price - (self.__price * item.discount)


    @classmethod              # Dcorator classmethod mean this code on scope class (no need parameter)
    def from_csv(cls):
        with open("CSV.csv","r") as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for i in items:
            item(
                name = i.get('name'),
                price = int(i.get('price')),
                quantity = i.get('quantity'),
            )

        print(f"Dis = {cls.discount}")        # this is can access discount cause this def on scope class


    @staticmethod           # Decorator staticmethod need parameter, on scope class
    def is_integer(num):
        if num % 1 == 0:
            return True
        else:
            return False

    # this def is print total list 
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"


    @property                # decorator for Read-only attribute if without SETTER property on below
    def name(self):         # cannot chance name twice
        return self.__name

    @name.setter            # decorator for chance the name
    def name(self, chance):
        if len(chance) > 5:
            raise Exception("Thats too long bitch !!!")
        self.__name = chance

    @property
    def price(self):
        return self.__price


    # SIMULATION SEND EMAIL TO USER
    def __send(self):
        pass

    def __connect(self, smtp_server):
        pass

    def __prepare_body(self):
        return f"""
        Hello you.
        We have {self.name} {self.quantity} times.

        Regards, Wiki from Wiki's.
        """

    # abstraction example
    def send_email(self):
        self.__connect('')
        self.__prepare_body()
        self.__send()


# NOTE
# * double underscore (__) : private attribute/method
# * method : fungsi yang berada di dalam class
# * @ : Decorator

# Encaptulation : tidak langsung mengubah private attribute tapi menggunakan
#                 method untuk mengubahnya.
#                 Contoh : attribute price diubah menggunakan method Discount()

# Abstraction : Menyembunyikan unecessary info from instances
#               user tidak perlu tau proses connect, prepare_body dan send
#               user hanya tau kalau dia dikirimi email (send_email)

# Inheritance : reuse code accros our classes (parent,child)
#               akses parent class melalui child. Buka file HP untuk contoh

# Polymorphisme : Jumlah item (total) dan jumlah HP rusak (hp_total) adalah contoh
#                 method sama calculate_total tpi beda value sesuai objek