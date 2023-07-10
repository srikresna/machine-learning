import csv

def baca_file_csv(nama_file):
    try:
        with open(nama_file, 'r') as file_csv:
            reader = csv.reader(file_csv)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("File tidak ditemukan.")

# Panggil fungsi baca_file_csv dengan nama file "SISISEGITIGA.csv"
baca_file_csv("python\data\SISISEGITIGA.csv")
