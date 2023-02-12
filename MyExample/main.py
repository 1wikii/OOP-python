# Diskon dari penulis
# Carlos  =  10%
# Farhan  =  30%
# Budi    =  50%

from administrasi import buku
from BUDI import budi
from FARHAN import farhan
from CARLOS import carlos


def title(chr):
    if chr == "A":
        return "AOV for live"
    elif chr == "S":
        return "Steam wallet are my treasure"
    elif chr == "Y":
        return "YUGIOH is good for phycology"


while True:

    print("=================================")
    print("\tPerpustakaan ITERA")
    print("=================================")
    print("\t   List Book:\n")
    print("|A302| AOV for live \n|S311| Steam wallet are my treasure \n|Y611| YUGIOH is good for phycology")
    print("=================================")

    print("\tPurchase Orders\n")
    print("press 1 to stop shopping !\n")
    buy = input("Enter code of book : ")

    # STOP PROGRAM
    if buy == "1":
        break

    amount = int(input("How many : "))

    for i in range(1, amount+1):
        if buy == 'A302':
            A = budi(title('A'),"BUDI",2023,50)
            A.DISKON()
        elif buy == 'S311':
            S = farhan(title('S'),"FARHAN",2023,100)
            S.DISKON()
        elif buy == 'Y611':
            Y = carlos(title('A'),"CARLOS",2023,400)
            Y.DISKON()

    print("\nHere youre purchased \/")
    print(buku.jumlah_buku)

    input()

print("=================================")
print("Pay => " + str(buku.bayar))
print("=================================")



