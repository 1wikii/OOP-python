

class akunbank:
    list_pelanggan = []         # row untuk setiap akun, isi row 0 no, 1 nama, 2 saldo
    def __init__(self,no , nama , saldo):
        self.__no_pelanggan = no 
        self.__nama_pelanggan = nama
        self.__jumlah_saldo = saldo 
        
        akunbank.list_pelanggan.append([self.__no_pelanggan,self.__nama_pelanggan, self.__jumlah_saldo])
        
    def lihat_menu(self):
        pil = input('1. lihat saldo\n2. tarik tunai\n3. transfer saldo\n4. keluar\nMasukan input : ')
        return pil
        
    def lihat_saldo(self):
        return self.__jumlah_saldo
        
    def tarik_tunai(self):
        tarik = int(input('Jumlah tarik tunai : '))
        if tarik > self.__jumlah_saldo:
            print('Saldo kurang!')
            self.tarik_tunai()
        else:
            self.__jumlah_saldo -= tarik
            print('Berhasil melakukan penarikan!')
            
    def transfer(self,penerima="obj",jumlah=-1):
    
        if jumlah == -1:
        
            tujuan = input('Nomor rekening tujuan : ')
            for akun in akunbank.list_pelanggan:
                if str(akun[0]) == tujuan:
                    return akun[1]
                    break
                
            print('nomor tidak ditemukan!')
            self.transfer()
            
        elif jumlah >= 0:
            self.__jumlah_saldo -= jumlah
            penerima.__jumlah_saldo += jumlah

kamu = akunbank(1211,input('Nama kamu : '),1000)
ukraina = akunbank(3222,"ukraina",500)
elon = akunbank(99,"elon musk",200)

def transaksi():
    pil = kamu.lihat_menu()
    
    if pil == '1':
        print("Saldo = ",kamu.lihat_saldo())
        transaksi()
    elif pil == '2':
        kamu.tarik_tunai()
        transaksi()
    elif pil == '3':
        org = kamu.transfer()

        if org == "ukraina":
            kamu.transfer(penerima=ukraina,jumlah=int(input('jumlah : ')))
            print("saldo penerima :",ukraina.lihat_saldo())

        elif org == "elon musk":
            kamu.transfer(penerima=elon,jumlah=int(input('jumlah : ')))
            print("saldo penerima :",elon.lihat_saldo())
            
        transaksi()
    else:
        pass
        
    
transaksi()
        
        
        

