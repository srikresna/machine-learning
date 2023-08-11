with open("test.txt", "w", encoding="utf-8") as file:
    file.write("Hello World")

# pakai append
with open("test.txt", "a", encoding="utf-8") as file:
    file.write("\nHello World")

# tambah lagi 
with open("test.txt", "a", encoding="utf-8") as file:
    file.write("\nHello World 2")

# pakai r+
with open("test.txt", "r+", encoding="utf-8") as file:
    file.write("\nHello World 3")
    file.write("\nHello World 4")

with open("test.txt", "r+", encoding="utf-8") as file:
    data = file.read()
    print(data)

with open("test.txt", "r+", encoding="utf-8") as file:
    file.write("\nHello World 5") # menimpa isi teks susuai dengan posisi kursor