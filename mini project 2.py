from prettytable import PrettyTable
import os
os.system("cls")

def timezone():
    print("================= TIMEZONE =================")

# Database sederhana dari barang-barang hadiah
tabel_barang = PrettyTable()
tabel_barang.field_names = ["No.", "Daftar Hadiah", "Tiket Diperlukan"]

def hadiah_list (nomor_hadiah, nama_hadiah, tiket_barang):
    tabel_barang.add_row([nomor_hadiah, nama_hadiah, tiket_barang])
hadiah_list("1", "Pulpen", "65")
hadiah_list("2", "Rubik", "250")
hadiah_list("3", "HotWheel", "550")
hadiah_list("4", "Sepeda", "5000")
hadiah_list("5", "PS 5", "20000")
hadiah_list("6", "Vario", "30000")
hadiah_list("7", "Lenovo Legion", "60000")
hadiah_list("8", "VR", "80000")
hadiah_list("9", "Honda Brio", "200000")
hadiah_list("10", "Honda Civic Turbo", "500000")

# Fitur Admin Untuk Menambahkan Hadiah (Create)
def tambah_hadiah():
    nomor_hadiah = input("Masukan Nomor Barang Baru: ")
    nama_hadiah = input("Masukan Nama Barang Baru: ")
    tiket_barang = int(input("Masukan Jumlah Tiket Yang Diperlukan: "))
    hadiah_list (nomor_hadiah, nama_hadiah, tiket_barang)
    print(f"Hadiah {nama_hadiah} dengan tiket sebanyak {tiket_barang} berhasil ditambahkan!")
    print("\n")

# Fitur Admin Untuk Melihat Hadiah (Read)
def lihat_hadiah():
    print(tabel_barang)

# Fitur Admin Untuk Memperbarui Hadiah (Update)
def perbarui_hadiah():
    lihat_hadiah()
    nomor_hadiah = input("Masukan Nomor Hadiah: ")
    ubah_hadiah_harga = input("Pilih yang akan diubah (nama/harga): ")
    nilai_baru = input(f"Masukan {ubah_hadiah_harga} baru: ")
    for row in tabel_barang._rows:
        if row[0] == nomor_hadiah:
            index = tabel_barang._rows.index(row)
            if ubah_hadiah_harga == "nama":
                tabel_barang._rows[index][1] = nilai_baru
            elif ubah_hadiah_harga == "harga":
                tabel_barang.rows[index][2] = nilai_baru
            else:
                print ("Data Tidak Valid")
                return perbarui_hadiah()
    print(f"Hadiah dengan Nomor {nomor_hadiah} berhasil diubah")
    print("\n")

# Fitur Admin Untuk Menghapus Hadiah (Delete)
def hapus_hadiah():
    while True:
        lihat_hadiah()
        nomor_hadiah = input("Masukan hadiah yang ingin dihapus: ")
        for row in tabel_barang._rows:
            if row[0] == nomor_hadiah:
                tabel_barang.del_row(tabel_barang.rows.index(row))
                print(f"Hadiah dengan Nomor {nomor_hadiah} telah dihapus")
                print("\n")
                break
        else:
            print("Hadiah tidak ditemukan")
        break

# Membuat program login untuk admin dan user
def login():
    while True:
        print("========= LOGIN =========")
        print("Silahkan Pilih Role Anda: ")
        tabel_login = PrettyTable()
        tabel_login.field_names = ["No.", "Role Anda"]
        tabel_login.add_row(["1", "Admin"])
        tabel_login.add_row(["2", "Customer"])
        print(tabel_login)
        pilihan = input("Masukan Pilihan Role Anda (1 atau 2): ")
        print("\n")
        if pilihan == "1":
            admin()
        elif pilihan == "2":
            customer()
            break
        else:
            print("\nPilihan Role Tidak Ada, Silahkan Login Kembali")
            return login()

# Fitur Menu Untuk Admin
def admin():
    while True:
        print("===== ADMIN TELAH DATANG! =====")
        tabel_admin = PrettyTable()
        tabel_admin.field_names = ["No.", "Menu"]
        tabel_admin.add_row(["1", "Tambah Hadiah Baru"])
        tabel_admin.add_row(["2", "Lihat Daftar Hadiah"])
        tabel_admin.add_row(["3", "Perbarui Hadiah"])
        tabel_admin.add_row(["4", "Hapus Hadiah"])
        tabel_admin.add_row(["5", "Kembali Ke Menu Login"])
        tabel_admin.add_row(["6", "Keluar"])
        print(tabel_admin)
        pilihan_admin = input("Pilih Menu: ")
        if pilihan_admin == "1":
            tambah_hadiah()
        elif pilihan_admin == "2":
            timezone()
            lihat_hadiah()
            timezone()
            print("\n")
        elif pilihan_admin == "3":
            perbarui_hadiah()
        elif pilihan_admin == "4":
            hapus_hadiah()
        elif pilihan_admin == "5":
            print("Anda Akan Diarahkan Ke Menu Login")
            print("\n")
            login()
            exit()
        elif pilihan_admin == "6":
            print("Terima kasih telah menggunakan sistem kami!")
            exit()
        else:
            print("Pilihan Menu Tidak Tersedia.")

# Menu Untuk Customer
def customer():
    print("------------------- SELAMAT DATANG! -------------------")
    tiket_user = int(input("Masukkan jumlah tiket Anda: "))
    print("\n")
    while True:
        timezone()
        lihat_hadiah()
        timezone()
        nomor_hadiah = input("Masukkan nomor hadiah yang ingin ditukar: ")
        print("\n")
        for row in tabel_barang._rows:
            if row[0] == nomor_hadiah:
                tiket_barang = int(row[2]) 
                if tiket_user >= tiket_barang:
                    tiket_user -= tiket_barang
                    print(f"Anda berhasil menukar {tiket_barang} tiket dengan barang {row[1]}!")
                    print(f"Sisa tiket Anda: {tiket_user}")
                else:
                    print(f"Maaf, Anda tidak memiliki cukup tiket untuk menukar {row[1]}.")
                break
        else:
            print("Barang tidak tersedia, silakan masukkan nomor yang benar.")
        # Pilihan apakah ingin menukar hadiah lagi atau tidak
        lanjut = input("Apakah Anda ingin menukar hadiah lain? (y/n): ")
        if lanjut != 'y':
            print("\n")
            print("Terima kasih telah menggunakan sistem kami!")
            print("------------------- SAMPAI JUMPA KEMBALI! -------------------")
            break

#Menjalankan Program
login()