from administrasi import buku 

class budi(buku):

    diskon = 0.5
    bayar = 0

    def __init__(self,nama: str, pengarang: str, tahun_terbit: int, harga: int) -> None:

        super(budi,self).__init__(
            nama,pengarang,tahun_terbit,harga
        )

    def DISKON(self):
	    self.harga = self.harga*budi.diskon
	    buku.bayar += self.harga