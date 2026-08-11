#           Variabel & Tipe Data (Kotak Penyimpanan)



#       Variabel

# VARIABEL = KOTAK PENYIMPANAN dengan LABEL/NAMA
# nama = "Rajif"
# ↑       ↑     ↑
# Nama    =     Isi
# kotak        yang
#             disimpan


#       5 Jenis Tipe Data Utama Python

#   1. String (str) --> Teks / Kata-kata
# selalu dibungkus dengan tanda petik ' atau "
# contohnya:
# "Halo" , 'Rajif' , "123" -> BUKAN angka, ada petik = teks
# Operasi yang BISA: 
# - Gabung teks: "ha" + "lo" = "halo"
# - Ulang teks: "ha" x 3 = "hahaha"
# Ambil bagian: "halo"[10] = "h"
# Operasi yang TIDAK BISA:
# - Dijumlahkan = "5" + "3" = "53" (bukan 8)
# - Dikurangi = "10" - "3" = ERROR!

#   2. INTEGER (int) --> Angka Bulat (tidak ada koma)
# TIDAK perlu petik
# contohnya: 5 , 10, -15 , 0
# TIDAK ada 1.5 (desimal)
# Operasi yang bisa:
# - Tambah: 5 + 3 = 8
# - Kurang: 10 - 4 = 6
# - Kali: 7 x 3 = 21
# - Bagi: 15/3 = 5
# - Sisa bagi: 17 % 5 = 2

#   3. FLOAT (float) --> Angka desimal (ada titik/koma)
# TIDAK perlu petik
# contohnya: 3.14 , 0.5 , 100.0
# bisa untuk pengukurang yang lebih presisi
# Operasi yang bisa sama dengan INTEGER tetapi hasilnya bisa desimal
# cth: 7/2 = 3.5 , 0.1 + 0.2 = 0.3000000 (kadang aneh)

#   4. BOOLEAN (bool) --> Benar atau Salah
# hanya ada 2 nilai: True (benar) atau False (salah)
# huruf awal HARUS BESAR, TIDAK pakai petik
# Analoginya seperti saklar lampu, NYALA atau MATI
# tidak ada 'setengah nyala'
# Biasa hasil dari PERBANDINGAN:
# - 5 > 3 --> True
# - 5 < 3 --> False
# - 10 == 10 --> True
# Operasi yang bisa:
# - and: True and False = False
# - or: True or False = True
# - not: not True = False

#   5. None --> Tidak ada apa-apa / kosong / null
# Huruf awal BESAR, TIDAK pakai petik
# contoh: x = None
# Analoginya KOSONGAN, belum ada isinya, nanti diisi
# Penggunaan:
# - Variabel belum ada nilai (placeholder)
# - Fungsi tidak mengembalikan apa-apa
# - Parameter opsional tidak diisi


#       Fungsi type() - Cek Tipe Data
type("Halo")     # → <class 'str'>      (string)
type(100)       # → <class 'int'>      (integer)
type(3.14)      # → <class 'float'>    (float)
type(True)       # → <class 'bool'>     (boolean)
type(None)       # → <class 'NoneType'> (none)


