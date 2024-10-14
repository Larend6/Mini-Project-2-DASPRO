# Mini-Project-2-DASPRO
Narendra Augusta Srianandha | 2409116010 | Kelas: A | Tema: Sistem Penukaran Tiket Timezone

# Flowchart
![minpro 2 drawio (5)](https://github.com/user-attachments/assets/98f1705a-2cfa-4b6c-b5ec-f642319b5731)

# Penjelasan Output
## Login
![image](https://github.com/user-attachments/assets/30389acf-825b-4933-94cb-12ee5f3fb217) <br>
Terdapat 2 pilihan role yaitu Admin dan Customer yang masing-masing memiliki fungsinya sendiri:
1. Admin: Dapat melakukan CRUD, yaitu menambahkan, melihat, memperbarui, dan menghapus program
2. Customer: Hanya dapat melakukan program penukaran tiket saja

### Tampilan Menu Role Admin
![image](https://github.com/user-attachments/assets/098a0ea4-240f-4925-abc4-b469f444f9ef) <br>
Pada menu admin, terdapat 6 fitur seperti ada sistem CRUD dan tambahan fitur kembali ke menu login dan fitur keluar dari program

### Tampilan Menu Role Customer
![image](https://github.com/user-attachments/assets/57a67b31-75a0-4d32-8fd3-f806d96483c0) <br>
Pada menu customer, user langsung diminta untuk mengisi jumlah tiket yang dimmiliki dikarenakan role customer hanya bisa melakukan transaksi tukar tiket berbeda dengan role admin yang memiliki banyak fitur

### Tampilan Ketika User Menginputkan Selain Admin dan Customer
![image](https://github.com/user-attachments/assets/c2e69bb1-db5e-41b7-903c-155dc2b886c9) <br>
Apabila user salah memasukan inputan selain admin dan customer, maka program akan otomatis meminta user untuk login lagi

# Penjelasan Menu Admin
## Tambah Hadiah Baru (Create)
![image](https://github.com/user-attachments/assets/18b29fa3-7380-41c9-b70a-059b4e90af8c) <br>
Setelah admin menginput fitur tambah maka admin akan langsung diminta untuk menambahkan nomor barang, nama barang, dan jumlah tiket yang diperlukan <br>
![image](https://github.com/user-attachments/assets/8283e027-8344-4261-8dcd-12afd34758fd) <br>
Barang telah berhasil ditambahkan, untuk mengecek barang yang sudah ditambahkan maka admin melihatnya di fitur lihat daftar hadiah

## Lihat Daftar Hadiah (Read)
Pada fitur ini, program menampilkan tabel dari daftar barang-barang yang ada bahkan barang yang sudah ditambahkan pun ada seperti barang "Kingfinix Note 40 Pro" yang baru saja ditambahkan pada fitur tambah barang tadi
### Sebelum barang ditambah
![image](https://github.com/user-attachments/assets/d15c92d9-db43-4735-890f-c9584e29aefa)
### Setelah barang ditambah
![image](https://github.com/user-attachments/assets/922bf74e-36c3-40dd-a481-7841d2d6306e)

## Perbarui Hadiah (Update)
Mirip seperti fitur tambah barang, pada fitur ini admin diminta untuk memasukan nomor hadiah yang ingin diperbarui <br>
![image](https://github.com/user-attachments/assets/e283b56c-a393-427a-8a83-5b5bb72e8bce) <br>
Setelah itu admin juga diminta untuk memilih apakah yang ingin diganti itu nama atau harga dari hadiah tersebut dan setelah memilih, admin diminta untuk memasukan nama atau harga yang baru untuk diganti berikutnya
### Mengganti Nama Hadiah
![image](https://github.com/user-attachments/assets/676acc82-f661-46c1-ada1-8a0a1b1dc046) <br>
### Mengganti Harga Hadiah
![image](https://github.com/user-attachments/assets/f7805211-a074-4229-b78b-f2e8e85fcb2a) <br>
### Sebelum Hadiah Diperbarui
![image](https://github.com/user-attachments/assets/1aa1ae12-791f-4fd3-9c2d-2a1329fe5b3d) <br>
### Setelah Hadiah Diperbarui
![image](https://github.com/user-attachments/assets/cb3b9d3a-80a1-4edb-81e2-86dc302e775e) <br>

## Hapus Hadiah (Delete)
Pada fitur hapus atau delete, admin diminta untuk menginput hadiah mana yang ingin dihapus <br>
![image](https://github.com/user-attachments/assets/f12d2fd3-7bd5-4812-a14c-3be428523b5f) <br>
Hadiah berhasil dihapus setelah admin input hadiah yang telah dipilih <br>
![image](https://github.com/user-attachments/assets/cc24ce92-8718-4b8b-9a34-1d2bf1f12d1f) <br>
![image](https://github.com/user-attachments/assets/83e8c4b3-4389-4c2b-b6bf-99d79127c61f) <br>
Dapat dilihat pada gambar diatas bahwa pilihan hadiah nomor 11 sudah tidak ada lagi atau telah terhapus

## Kembali Ke Menu Login
Fitur ini dapat mengembalikan admin ke menu login lagi dan user dapat memilih untuk menjadi admin lagi atau ganti jadi customer <br>
![image](https://github.com/user-attachments/assets/c841a407-2e1a-4911-8cc3-5cd37f49b93c) <br>

## Fitur Keluar
Setelah admin tidak ada lagi yang ingin dilakukan di menu admin maka admin dapat memilih untuk keluar dari program <br>
![image](https://github.com/user-attachments/assets/4f2b2280-7a24-499a-a6db-989bd3f50182)

# Penjelasan Menu Customer
## Tampilan dari Penukaran Tiket Menjadi Hadiah
![image](https://github.com/user-attachments/assets/54e11b9b-b81c-4883-b9b5-39d7dbbd5d06) <br>
Setelah user memilih role menjadi customer, customer langsung diminta untuk mengisi jumlah tiket yang dia miliki yang setelahnya tiket tersebut akan ditukar dengan barang yang customer inginkan <br>
![image](https://github.com/user-attachments/assets/aa62de4d-2360-4c4d-9482-bb4e895a9b5e) <br>
Setelah mengisi jumlah tiket maka program akan menampilkan tabel dari daftar hadiah yang ada dan customer diminta untuk memilih hadiah mana yang dia inginkan <br>
![image](https://github.com/user-attachments/assets/840d7bc1-186f-4d3f-98f0-7589a4eaba9e) <br>
Customer berhasil mendapatkan barang yang dia inginkan dan pada programnya juga dijelaskan berapa sisa dari tiket yang dia miliki. Customer juga diberi pilihan apakah ingin menukar hadiah lain lagi atau tidak, apabila customer tetap melanjutkan untuk menukar hadiah lain tapi dengan sisa tiket yang tidak mencukupi maka customer tidak akan mendapatkan barang yang dia inginkan dan program masi menanyakan apakah ingin menukar lagi atau tidak, jika tidak maka program selesai dan akan muncul ucapan selamat tinggal <br>
![image](https://github.com/user-attachments/assets/e8f228b6-6fad-4945-9268-2a6510e83790)

## Tampilan dari Permintaan Diluar Daftar Barang
![image](https://github.com/user-attachments/assets/f1b57fcd-1988-4eea-8687-00478e5979e3) <br>
Apabila customer mengisi nomor hadiah selain dari yang di tabel maka output yang didapatkan adalah barang tidak tersedia dan customer diminta untuk menukar hadiah lain atau tidak









