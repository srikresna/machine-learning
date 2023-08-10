import datetime
import os
import random

# template 
mahasiswa_template = {
    'nama': 'nama',
    'nim': '000000000',
    'sks_lulus': 0,
    'lahir':datetime.datetime(1111, 1, 1),
}

data_mahasiswa = {}

# input data
while True:
    os.system('cls')
    print(f"{'SELAMAT DATANG DI PROGRAM INPUT DATA MAHASISWA':^20}")
    print(f"{'DATA MAHASISWA':^20}")
    print("-"*20)

    mahasiswa = dict.fromkeys(mahasiswa_template.keys())
    #random key
    mahasiswa['nama'] = input("Nama: ")
    nim = input("NIM: ")
    if len(nim) == 9:
        mahasiswa['nim'] = nim
    else:
        print("NIM harus 9 digit")
    mahasiswa['sks_lulus'] = int(input("SKS Lulus: "))
    TAHUN_LAHIR = int(input("Tahun Lahir (YYYY): "))
    BULAN_LAHIR = int(input("Bulan Lahir (MM): "))
    if BULAN_LAHIR > 12:
        print("Bulan tidak boleh lebih dari 12")
        BULAN_LAHIR = int(input("Bulan Lahir (MM): "))
    TANGGAL_LAHIR = int(input("Tanggal Lahir (DD): "))
    if TANGGAL_LAHIR > 31:
        print("Tanggal tidak boleh lebih dari 31")
        TANGGAL_LAHIR = int(input("Tanggal Lahir (DD): "))
    mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR, BULAN_LAHIR, TANGGAL_LAHIR)

    # random key
    KEY = random.randint(1000, 9999)
    data_mahasiswa.update({KEY: mahasiswa})

    print(f"{'KEY':<9} {'NAMA':<10}{'NIM':<15}{'SKS':<5}{'LAHIR':<10}")
    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa
        NAMA = data_mahasiswa[KEY]['nama']
        NIM = data_mahasiswa[KEY]['nim']
        SKS = data_mahasiswa[KEY]['sks_lulus']
        LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%d-%m-%Y")
        print(f"{KEY:<9} {NAMA:<10}{NIM:<15}{SKS:<5}{LAHIR:<10}")

    
    print("-"*20)
    is_done = input("Tambah data lagi? (y/n): ")
    if is_done == 'n':
        break

print("THANKKKKSSSSSSS")