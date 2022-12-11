import random
import datetime
from customer import Customer

atm = Customer(id)

while True:
    id = int(input("Masukkan pin Anda: "))
    trial = 0

    while id != int(atm.checkPin()) and trial < 3:
        id = int(input("Pin Anda salah.\nSilakan Masukkan pin Anda lagi: "))
        trial += 1

        if trial == 3:
            print("Error. Silakan ambil kartu dan coba lagi..")
            exit()

    while True:
        print("Selamat datang di ATM! Berikut fitur yang tersedia...")
        print(
            "\n1 - Cek Saldo \t 2 - Tarik Tunai \t 3 - Setor Tunai \n4 - Ganti Pin \t 5 - Keluar "
        )
        selectmenu = int(input("\nSilakan pilih menu: "))
        if selectmenu == 1:
            print("Sisa saldo Anda sekarang: Rp." + str(atm.checkBalance()))
            print(
                "----------------------------------------------------------------------------------"
            )

        elif selectmenu == 2:
            nominal = int(input("Masukkan nominal yang ingin Anda ambil: "))
            verify_withdraw = input(
                "Konfirmasi: Anda akan melakukan tarik tunai dengan nominal berikut? \nRp."
                + str(nominal)
                + " [y/n]: "
            )

            if verify_withdraw == "y":
                print("Saldo awal anda adalah: Rp." + str(atm.checkBalance()) + "")
            else:
                break
            if nominal < atm.checkBalance():
                atm.withdrawBalance(nominal)
                print("Transaksi tarik tunai berhasil!")
                print("Sisa saldo Anda sekarang: Rp." + str(atm.checkBalance()) + "")
            else:
                print("Maaf. Saldo anda tidak cukup untuk melakukan tarik tunai!")
                print("Silakan lakukan setor tunai terlebih dahulu")
            print(
                "----------------------------------------------------------------------------------"
            )

        elif selectmenu == 3:
            nominal = int(input("Masukkan nominal yang ingin Anda setor: "))
            verify_deposit = input(
                "Konfirmasi: Anda akan mmelakukan setor tunai degan nominal berikut? \nRp."
                + str(nominal)
                + " [y/n]: "
            )

            if verify_deposit == "y":
                atm.depositBalance(nominal)
                print(
                    "Sisa saldo Anda sekarang adalah: Rp."
                    + str(atm.checkBalance())
                    + "\n"
                )
            else:
                break
            print(
                "----------------------------------------------------------------------------------"
            )

        elif selectmenu == 4:
            verify_pin = int(input("Masukkan pin lama anda   : "))

            while verify_pin != int(atm.checkPin()):
                print("Pin yang Anda masukkan salah, silakan masukkan pin: ")

            updated_pin = int(input("Silakan masukkan pin baru: "))
            print("Pin Anda berhasil diganti!")

            verify_newpin = int(input("Coba masukkan pin baru: "))
            if verify_newpin == updated_pin:
                print("Pin baru Anda sesuai!")
            else:
                print("Maaf, pin Anda salah! ")
            print(
                "----------------------------------------------------------------------------------"
            )

        elif selectmenu == 5:
            print(
                "Resi tercetak otomatis saat anda keluar. \nHarap simpan tanda terima ini sebagai bukti transaksi anda."
            )
            print("No. Record : ", random.randint(100000, 1000000))
            print("Tanggal    : ", datetime.datetime.now())
            print("Saldo akhir: ", atm.checkBalance())
            print("Terima kasih telah menggunakan ATM!")
            print(
                "----------------------------------------------------------------------------------"
            )
            exit()
        else:
            print("Error. Maaf, menu tidak tersedia")
            print(
                "----------------------------------------------------------------------------------"
            )
