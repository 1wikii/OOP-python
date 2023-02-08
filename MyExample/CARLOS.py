from administrasi import buku 

class carlos(buku):

    diskon = 0.9

    def __init__(self,nama: str, pengarang: str, tahun_terbit: int, harga: int) -> None:

        super().__init__(
            nama,pengarang,tahun_terbit,harga
        )