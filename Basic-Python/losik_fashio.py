# Import library
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# funsgi login
def login():
    for i in range(3):
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        if username == "admin" and password == "admin":
            return True
        else:
            print("Username atau password salah!")
    print("Anda telah melakukan login sebanyak 3 kali, sesi login telah berakhir!")
    return False

# fungsi menu utama
def menu():
    print("Menu Utama")
    print("1. Edit Data")
    print("2. Perhitungan Harga Jual Produk")
    print("3. Keluar")
    pilihan = int(input("Masukkan pilihan: "))
    return pilihan

# buat dummy data
data = {
    'Nama Produk': ['Kaos', 'Celana', 'Jaket', 'Kemeja'],
    'Detail Komponen': ['Bahan: katun, Kain: katun, Warna: putih, Ukuran: M, L, XL', 'Bahan: katun, Kain: katun, Warna: hitam, Ukuran: M, L, XL', 'Bahan: katun, Kain: katun, Warna: putih, Ukuran: M, L, XL', 'Bahan: katun, Kain: katun, Warna: putih, Ukuran: M, L, XL']
}
df = pd.DataFrame(data)
df.to_excel('data.xlsx', index=False)


# fungsi menampilkan rincian data nama produk dan detail komponennya dalam bentuk tabel
def tampilkan_data():
    df = pd.read_excel('data.xlsx')
    print(df)

# fungsi edit data
def edit_data():
    print("Menu Edit Data")
    print("1. Tambah Data")
    print("2. Ubah Data")
    print("3. Kembali")
    pilihan = int(input("Masukkan pilihan: "))
    return pilihan

# fungsi tambah data
def tambah_data():
    df = pd.read_excel('data.xlsx')
    nama_produk = input("Masukkan nama produk: ")
    detail_komponen = input("Masukkan detail komponen: ")
    df = df.append({'Nama Produk': nama_produk, 'Detail Komponen': detail_komponen}, ignore_index=True)
    df.to_excel('data.xlsx', index=False)
    print("Data berhasil ditambahkan!")
    print(df)

# fungsi ubah data
def ubah_data():
    df = pd.read_excel('data.xlsx')
    print(df)
    nama_produk = input("Masukkan nama produk yang ingin diubah: ")
    detail_komponen = input("Masukkan detail komponen: ")
    df.loc[df['Nama Produk'] == nama_produk, 'Detail Komponen'] = detail_komponen
    df.to_excel('data.xlsx', index=False)
    print("Data berhasil diubah!")
    print(df)

# menampilkan nama produk yang tersedia pada data perusahaan
def tampilkan_nama_produk():
    df = pd.read_excel('data.xlsx')
    print(df['Nama Produk'])

# fungsi perhitungan harga jual produk
def perhitungan_harga_jual_produk():
    df = pd.read_excel('data.xlsx')
    print(df['Nama Produk'])
    nama_produk = input("Masukkan nama produk: ")
    harga_pokok_produksi = int(input("Masukkan harga pokok produksi: "))
    jumlah_unit_produksi = int(input("Masukkan jumlah unit produksi: "))
    persentase_laba = int(input("Masukkan persentase laba: "))
    harga_penjualan_produk = harga_pokok_produksi + (harga_pokok_produksi * persentase_laba / 100)
    harga_penjualan_produk = harga_penjualan_produk / jumlah_unit_produksi
    print("Harga penjualan produk: ", harga_penjualan_produk)

    # membuat pie chart
    labels = 'Harga Pokok Produksi', 'Laba'
    sizes = [harga_pokok_produksi, harga_penjualan_produk - harga_pokok_produksi]
    explode = (0, 0.1)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')
    plt.show()

# main
if login():
    while True:
        pilihan = menu()
        if pilihan == 1:
            while True:
                pilihan = edit_data()
                if pilihan == 1:
                    tambah_data()
                elif pilihan == 2:
                    ubah_data()
                elif pilihan == 3:
                    break
                else:
                    print("Pilihan tidak tersedia!")
        elif pilihan == 2:
            perhitungan_harga_jual_produk()
        elif pilihan == 3:
            break
        else:
            print("Pilihan tidak tersedia!")    
"""
Algoritma Penentuan Harga Jual Produk pada Losik Fashion

Langkah 1: Mulai.
Langkah 2: Masukkan username dan password.

Langkah 3: Apakah username dan password sudah sesuai? Jika iya lanjut ke

langkah 6, jika tidak lanjut ke langkah 4.

Langkah 4: Apakah username dan password yang dimasukkan sudah salah
sebanyak 3 kali? Jika iya lanjut ke langkah 5, jika tidak menampilkan
“login gagal” dan kembali ke langkah 2.

Langkah 5: Menampilkan “sesi login telah berakhir!” kemudian lanjut ke langkah

25.

Langkah 6: Menampilkan menu program berupa menu edit data dan menu

perhitungan harga jual produk.

Langkah 7: Memilih menu edit data atau perhitungan.
Langkah 8: Apakah ingin melakukan edit data? jika iya lanjut ke langkah 9 , jika

tidak lanjut ke langkah 17

Langkah 9: Menampilkan rincian data nama produk dan detail komponennya

dalam bentuk tabel.

Langkah 10: Memilih menambahkan data atau mengubah data.
Langkah 11: Apakah ingin melakukan pertambahan data? jika iya lanjut ke langkah

12, jika tidak lanjut ke langkah 13.

Langkah 12: Memasukkan data yang ingin ditambah, kemudian lanjut ke langkah

14.

Langkah 13: Memasukkan data yang ingin diubah.
Langkah 14: Menampilkan data yang telah diperbarui.
Langkah 15: Menyimpan dalam file excel.
Langkah 16: Apakah anda ingin mengedit data lagi? Jika iya kembali ke langkah 9

jika tidak lanjut ke langkah 17.

Langkah 17: Menampilkan nama produk yang tersedia pada data perusahaan.
Langkah 18: Memilih nama produk.
Langkah 19: Memasukkan harga pokok produksi.
Langkah 20: Memasukkan jumlah unit produksi.
Langkah 21: Memasukkan persentase laba.
Langkah 22: Melakukan perhitungan harga penjualan produk dengan rumus

Harga penjualan produk =
Harga Pokok Produksi+(Harga Pokok Produksi x Presentase Laba)

Jumlah Unit Produksi

Langkah 23: Apakah ingin melakukan perhitungan kembali? jika iya kembali ke

langkah 17, jika tidak lanjut ke langkah 24.

Langkah 24: Menampilkan pie chart untuk memperlihatkan proporsi laba yang

didapatkan dan harga produksi yang dikeluarkan.

Langkah 25: Selesai.

"""

