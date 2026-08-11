#           Let's Practice!

# Perintah:
# BARIS 1: Buat variabel bernama nama_depan
#         Isi dengan NAMA DEPANMU (string/petak)
# BARIS 2: Buat variabel bernama umur
#         Isi dengan UMURMU (integer/tanpa petik)
# BARIS 3: Buat variabel bernama tinggi
#         Isi dengan TINGGI MU dalam meter (float/pakai titik!)
# BARIS 4: Buat variabel bernama mahasiswa
#         Isi dengan True atau False (boolean/hurus besar)
# BARIS 5: Kosongkan 1 baris
# BARIS 6: Tampilkan semua data menggunakan print:
#         Format: "Nama: [nama_depan]"
# BARIS 7: Tampilkan umur:
#         Format: "Umur: [umur] tahun"
# BARIS 8: Tampilkan tinggi:
#         Format: "Tinggi: [tinggi] m"
# BARIS 9: Tampilkan status mahasiswa:
#         Format: "Mahasiswa: [mahasiswa]"
# BARIS 10: Kosongkan 1 baris
# BARIS 11: Tampilkan TIPE DATA dari setiap variabel:
#         Gunakan fungsi type()
#         Format: "Tipe 'nama_depan': <class ...>"
# BARIS 12: Tipe data umur
# BARIS 13: Tipe data tinggi
# BARIS 14: Tipe data mahasiswa

#PETUNJUK:
# - String: "teks" atau 'teks'
# - Integer: 123 (tanpa petik)
# - Float: 1.75 (pakai titik . bukan koma ,)
# - Boolean: True atau False (huruf besar awal)
# - f-string: print(f"teks {variabel}")
# - type(): print(type(variabel))

#       BEGIN !

nama_depan = 'Rajif'
umur = 18
tinggi = 163.5
mahasiswa = True

print (f'Nama: {nama_depan}\n'
       f'Umur: {umur}\n'
       f'Tinggi: {tinggi}\n'
       f'Mahasiswa: {mahasiswa}\n')

print("Tipe 'nama_depan':", type(nama_depan))
print("Tipe 'umur':", type(umur))
print("Tipe 'tinggi':", type(tinggi))
print("Tipe 'mahasiswa':", type(mahasiswa))

# Output

# Nama: Rajif
# Umur: 18
# Tinggi: 163.5
# Mahasiswa: True

# Tipe 'nama_depan': <class 'str'>
# Tipe 'umur': <class 'int'>
# Tipe 'tinggi': <class 'float'>
# Tipe 'mahasiswa': <class 'bool'>

#       Explanation

# Baris 1 
# nama_depan = nama variabel (boleh lebih dari 1 kata, pakai _ pengganti spasi)
# memasukkan string

# Baris 2
# memasukkan integer

# Baris 3
# memasukkan float (desimal) dengan .

# Baris 4

# Baris 6-10
# menuliskan / print kata awalannya, 
# lalu menggunakan f string untuk menampilkan variabel didalam {}
# lalu menggunakan \n agar turun ke baris selanjutnya

# Penjelasan Apa Itu \n ?
# \n = NEWLINE (garis baru/enter)

# Beberapa Karakter Khusus Lainnya (Escape Characters)
# \n -> Newline -> Pindah ke baris baru -> "Halo\nDunia" -> 2 baris
# \t -> Tab -> Spasi besar -> "Nama:\tRajif" -> Nama:   Rajif
# \\ -> Backslash -> Tampilkan tanda \ "C:\\Users"-> C:\Users
# \' -> Single quote -> Tampilkan petik dalam teks -> 'It\'s' -> It's
# \" -> Double quote -> Tampilkan petik dalam teks -> "He said \"hi\""

# Baris 11-14
# Penjelasan mengapa pakai koma:
# print() bisa menerima LEBIH DARI 1 parameter
# sintaks: print(parameter_1, parameter_2, parameter_3)
# koma sebagai pemisah

# Kalau ada koma, python akan:
#- Tampilkan parameter_1
# - SPASI (otomatis)
# - Tampilkan parameter_2

# Jadi, koma sebagai pemisah sekaligus memberi spasi otomatis antara 
# string dan hasil type()
# Tanpa koma (gabung manual):
# print("Tipe:" + " " + str(type(x)))
# lebih ribet, hasil sama

# Bisa juga begini! menggunakan f-string
# print("Tipe: {type(nama_depan)}")

