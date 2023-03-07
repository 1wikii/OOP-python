class jeruk:
    diskon = 0.2  #diskon 20%
    def __init__(self,jenis: str, rasa: str,ukuran: str,harga: int):
        self.jenis = jenis
        self.rasa = rasa
        self.harga = harga
        self.ukuran = ukuran
        
    def cek_harga(self):
        self.diskon()
        if self.harga > 15000:
            print(f"jeruk {self.jenis} tidak worth it dan mahal, jgn beli!!")
        else:
            print(f"Rasanya {self.rasa},jeruk {self.jenis} sangat worth it, approve:v dan ukuranyapun {self.ukuran}")
    
    def diskon(self):
        if self.rasa == 'manis':
            self.harga += 5000
        else:
            self.harga *= jeruk.diskon

mang_budi = jeruk('sangkis','manis','badag',10000)
mang_budi.cek_harga()

   

