# import random as rd

# class Robot:
#     jumlah_turn = 0

#     def __init__(self, nama):
#         self.nama = nama
#         self.health = 0
#         self.damage = 0

#     def lakukan_aksi(self, lawan):
#         self.jumlah_turn += 1
#         print("Robot {} menyerang sebanyak {} DMG".format(self.nama, self.damage))
#         if self.jumlah_turn % 3 == 0:
#             print("Robot {} meningkatkan damage menjadi 1.5x lipat sementara".format(self.nama))
#             self.damage = int(self.damage * 1.5)
#         if self.jumlah_turn == 4 and isinstance(self, Lecalicus):
#             print("Robot {} meningkatkan damage menjadi 2x lipat sementara dan menambah darah sebanyak 7000 HP".format(self.nama))
#             self.health += 7000
#             self.damage *= 2
#         if self.jumlah_turn == 2 and isinstance(self, Alphasetia):
#             print("Robot {} menambah darah sebanyak 4000 HP".format(self.nama))
#             self.health += 4000
#         lawan.terima_aksi(self.damage)

#     def terima_aksi(self, damage):
#         self.health -= damage
#         if self.health < 0:
#             self.health = 0

# class Antares(Robot):
#     def __init__(self):
#         super().__init__("Antares")
#         self.health = 50000
#         self.damage = 5000

# class Alphasetia(Robot):
#     def __init__(self):
#         super().__init__("Alphasetia")
#         self.health = 40000
#         self.damage = 6000

# class Lecalicus(Robot):
#     def __init__(self):
#         super().__init__("Lecalicus")
#         self.health = 45000
#         self.damage = 5500

# def main():
#     print("Selamat datang di pertandingan robot Yamako")
#     print("Pilih robotmu (1 = Antares, 2 = Alphasetia, 3 = Lecalicus): ")
#     pilihan_robotmu = int(input())
#     if pilihan_robotmu == 1:
#         robotmu = Antares()
#     elif pilihan_robotmu == 2:
#         robotmu = Alphasetia()
#     elif pilihan_robotmu == 3:
#         robotmu = Lecalicus()
#     else:
#         print("Pilihan tidak valid")
#         return

#     print("Pilih robot lawan (1 = Antares, 2 = Alphasetia, 3 = Lecalicus): ")
#     pilihan_lawan = int(input())
#     if pilihan_lawan == 1:
#         lawan = Antares()
#     elif pilihan_lawan == 2:
#         lawan = Alphasetia()
#     elif pilihan_lawan == 3:
#         lawan = Lecalicus()
#     else:
#         print("Pilihan tidak valid")
#         return

#     for turn in range(1, 11):
#         print("\nTurn saat ini: {}".format(turn))
#         print("Robotmu ({} - {} HP), robot lawan ({} - {} HP)".format(robotmu.nama, robotmu.health, lawan.nama, lawan.health))
#         print("Pilih tangan robotmu ({}): ".format(robotmu.nama))
#         pilihan_robotmu = int(input())
#         pilihan_lawan = rd.randint(1,3)
#         if pilihan_robotmu == 1:
#             if pilihan_lawan == 1:
#                 print("Robotmu dan lawan sama-sama memilih gunting")
#             elif pilihan_lawan == 2:
#                 print("Robotmu memilih gunting, lawan memilih batu")
#                 lawan.lakukan_aksi(robotmu)
#             elif pilihan_lawan == 3:
#                 print("Robotmu memilih gunting, lawan memilih kertas")
#                 robotmu.lakukan_aksi(lawan)
#         elif pilihan_robotmu == 2:
#             if pilihan_lawan == 1:
#                 print("Robotmu memilih batu, lawan memilih gunting")
#                 robotmu.lakukan_aksi(lawan)
#             elif pilihan_lawan == 2:
#                 print("Robotmu dan lawan sama-sama memilih batu")
#             elif pilihan_lawan == 3:
#                 print("Robotmu memilih batu, lawan memilih kertas")
#                 lawan.lakukan_aksi(robotmu)
#         elif pilihan_robotmu == 3:
#             if pilihan_lawan == 1:
#                 print("Robotmu memilih kertas, lawan memilih gunting")
#                 lawan.lakukan_aksi(robotmu)
#             elif pilihan_lawan == 2:
#                 print("Robotmu memilih kertas, lawan memilih batu")
#                 robotmu.lakukan_aksi(lawan)
#             elif pilihan_lawan == 3:
#                 print("Robotmu dan lawan sama-sama memilih kertas")

#         if robotmu.health == 0:
#             print("Sayang sekali, robotmu {} kalah dalam pertandingan ini.".format(robotmu.nama))
#             break
#         elif lawan.health == 0:
#             print("Selamat, robotmu {} menang dalam pertandingan ini!".format(robotmu.nama))
#             break
#     print("\nPertandingan selesai")
	
# if __name__ == "__main__":
#     main()

