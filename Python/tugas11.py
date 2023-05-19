import csv
import math

def hitung_luas_segitiga(sisi_a, sisi_b, sisi_c):
    s = (sisi_a + sisi_b + sisi_c) / 2
    luas = math.sqrt(s * (s - sisi_a) * (s - sisi_b) * (s - sisi_c))
    return luas

def hitung_keliling_segitiga(sisi_a, sisi_b, sisi_c):
    keliling = sisi_a + sisi_b + sisi_c
    return keliling

def baca_file_csv(nama_file):
    try:
        with open(nama_file, 'r') as file_csv:
            reader = csv.DictReader(file_csv)
            
            # Menampilkan header
            header = ["No", "a", "b", "c", "Luas Segitiga", "Keliling Segitiga"]
            print("{:<5} {:<5} {:<5} {:<5} {:<13} {:<16}".format(*header))
            
            # Menampilkan data setiap baris
            for row in reader:
                sisi_segitiga = {
                    'a': int(row['a']),
                    'b': int(row['b']),
                    'c': int(row['c'])
                }
                luas = hitung_luas_segitiga(sisi_segitiga['a'], sisi_segitiga['b'], sisi_segitiga['c'])
                keliling = hitung_keliling_segitiga(sisi_segitiga['a'], sisi_segitiga['b'], sisi_segitiga['c'])
                print("{:<5} {:<5} {:<5} {:<5} {:<13.3f} {:<16}".format(row['No'], sisi_segitiga['a'], sisi_segitiga['b'], sisi_segitiga['c'], luas, keliling))
    except FileNotFoundError:
        print("File tidak ditemukan.")

# Panggil fungsi baca_file_csv dengan nama file "SISISEGITIGA.csv"
baca_file_csv("python\data\SISISEGITIGA.csv")
