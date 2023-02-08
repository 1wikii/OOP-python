from item import item 
from HP import HP


A = item("android",100,10)
B = HP("linux",200,10)
C = item("windows",300,10)

# ACCESS METHOD TO CALCULATE
# A.discount = 0.9
# print("price = ",end="")
# A.calculate_total()
# A.Discount()
# print( str(A.price) + " Dollar")


# PRINT TOTAL WITH LOOP USING MAGIC METHOD REPR
# for instance in item.total:
# print(instance, end=", \n")
# print(item.total)


# CSV AND IS_INTEGER METHOD
# item.from_csv()
# print(item.is_integer(7.5))


# ACCESS PARENT ADN CHILD CLASS
# print(item.total)
# print(HP.hp_total)


# USING PROPERTY TO LOCK NAME THEN CANNOT CHANCE

# A.name = "android"   # chance name goin' work cause SETTER PROPERTY
# print(A.name)
# A.price = 500		  # chance not work cause using decorator PROPERTY
# print(A.price)
