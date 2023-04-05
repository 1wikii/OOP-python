class mahasiswa:
    __jumlah = 0
    
    def __init__(self,nama: str, smt: int, umur: int):
        self.nama = nama
        self.__semester = smt
        self.__umur = umur
        
        mahasiswa.__jumlah += 1
    
    @property
    def umur(self):
        return self.__umur
    
    @property
    def semester(self) -> int:
        return self.__semester
    
    @semester.setter
    def set_smt(self, num) -> int:
        self.__semester = num
        
    def printout(self):
        print('Nama : ', self.nama)
        print('Umur : ', self.umur)
        print('Semester : ', self.semester)
        print('jumlah : ', mahasiswa.__jumlah,'\n')
        

def main():
    orang1 = mahasiswa("burhan", umur=18, smt=4)
    orang2 = mahasiswa("sambo", umur=32, smt=10)
    
    orang1.printout()
    orang2.printout()
    
    orang1.set_smt = int(input(f'\nset semester {orang1.nama}: '))
    orang2.set_smt = int(input(f'set semester {orang2.nama}: '))
    
    orang1.printout()
    orang2.printout()
    
main()
        
