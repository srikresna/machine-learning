# exception handling

# contoh di aplikasi try and catch
# while(True):
#     angka = int(input("Masukkan angka: "))
#     try:
#         hasil = 10/angka
#         print(f"hasil = {hasil}")
#         is_done = input("Apakah anda ingin keluar? (y/n): ")
#         if is_done == "y":
#             break
#     # error untuk input angka 0
#     except ZeroDivisionError:
#         print("Input tidak boleh 0")

# print("Selesai")


# contoh raise exception

# from numbers import Number

# def tambah(a, b):
#     if not isinstance(a, Number) or not isinstance(b, Number):
#         raise "Input harus angka"
#     return a + b

# print(tambah(1, 'a'))

angka = 'a'
try:
    hasil = 10/angka
except Exception as error_message:
    print(error_message)

# angka = 1
# try:
#     hasil = 10/angka
# except ZeroDivisionError as error_message:
#     print(error_message)
