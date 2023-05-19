# Membuka file
file_name = "python\data\SISISEGITIGA.txt"
try:
    file = open(file_name, "r")
except FileNotFoundError:
    print(f"File '{file_name}' tidak ditemukan.")
    exit()

# Membaca isi file
content = file.read()

# Menutup file
file.close()

# Menampilkan isi file ke layar
print(content)
