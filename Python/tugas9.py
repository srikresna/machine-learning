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
            reader = csv.reader(file_csv)
            next(reader)  # Skip header row
            for row in reader:
                sisi_segitiga = [int(x) for x in row[1:4]]  # Konversi sisi-sisi menjadi list
                luas = hitung_luas_segitiga(*sisi_segitiga)
                keliling = hitung_keliling_segitiga(*sisi_segitiga)
                print("Sisi-sisi segitiga:", sisi_segitiga)
                print("Luas segitiga:", luas)
                print("Keliling segitiga:", keliling)
                print()
    except FileNotFoundError:
        print("File tidak ditemukan.")

# Panggil fungsi baca_file_csv dengan nama file "SISISEGITIGA.csv"
baca_file_csv("python\data\SISISEGITIGA.csv")
