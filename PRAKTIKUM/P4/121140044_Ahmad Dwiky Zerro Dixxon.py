class bola:
    
    def __init__(self, jenis, berat):
        self.jenis = jenis
        self.berat = berat
        

class bola_kaki(bola):
    
    def __init__(self, jenis, berat, ukuran, jumlah):
        super().__init__(jenis,berat)
        self.ukuran = ukuran
        self.jumlah = jumlah
    
    def print(self):
        return (self.jenis,self.berat,self.ukuran,self.jumlah)

pemain = bola_kaki("nike",200, "besar", 9)

for p in pemain.print():
    print(p,end="  ")


