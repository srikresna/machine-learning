data_angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4]

print(data_angka)

# count data
print(f"Jumlah data angka 1: {data_angka.count(1)}")

# ambil posisi data
data = ["Ucup", "Sadam", "Rizal"]

print(data)

index_sadam = data.index("Sadam")
print(f"Index Sadam: {index_sadam}")

# mengurutkan list
print(f"Data sebelum diurutkan: {data_angka}")
data_angka.sort()
print(f"Data setelah diurutkan: {data_angka}")

# mengurutkan list huruf
print(f"Data sebelum diurutkan: {data}")
data.sort()
print(f"Data setelah diurutkan: {data}")

# membalik urutan list
print(f"Data sebelum dibalik: {data_angka}")
data_angka.reverse()
print(f"Data setelah dibalik: {data_angka}")

# copy list
data_angka2 = data_angka.copy()
print(f"Data angka 2: {data_angka2}")

# menghapus semua data
data_angka.clear()
print(f"Data angka setelah dihapus: {data_angka}")

# menggabungkan list
data_gabung = data_angka2 + data
print(f"Data gabungan: {data_gabung}")

# menghitung panjang list
print(f"Panjang data gabungan: {len(data_gabung)}")