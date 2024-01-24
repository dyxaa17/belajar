# Fungsi untuk penjumlahan
def tambah(x, y):
    return x + y
   
# Fungsi untuk pengurangan
def kurang(x, y):
    return x - y

# Fungsi untuk perkalian
def kali(x, y):
    return x * y

# Fungsi untuk pembagian
def bagi(x, y):
    if y != 0:
        return x / y
    else:
        return "Tidak bisa dibagi oleh 0"

# Menampilkan menu operasi
def menu_operasi():
    print("Pilih operasi:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Keluar")

# Program utama
while True:
    # Menampilkan menu operasi
    menu_operasi()

    # Input pilihan operasi dari pengguna
    pilihan = input("Masukkan pilihan (1/2/3/4/5): ")

    # Keluar dari program jika pengguna memilih 5
    if pilihan == '5':
        print("Keluar dari kalkulator. Terima kasih!")
        break

    # Input dua angka
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))

    # Melakukan operasi sesuai pilihan pengguna
    if pilihan == '1':
        print(angka1, "+", angka2, "=", tambah(angka1, angka2))
    elif pilihan == '2':
        print(angka1, "-", angka2, "=", kurang(angka1, angka2))
    elif pilihan == '3':
        print(angka1, "*", angka2, "=", kali(angka1, angka2))
    elif pilihan == '4':
        print(angka1, "/", angka2, "=", bagi(angka1, angka2))
    else:
        print("Pilihan tidak valid. Silakan masukkan angka 1-5.")
