from administrasi import buku 

class farhan(buku):
    
    diskon = 0.7

    def __init__(self,nama: str, pengarang: str, tahun_terbit: int, harga: int) -> None:

        super(farhan,self).__init__(
            nama,pengarang,tahun_terbit,harga
        )