'''lambda function'''
import os

os.system("cls")
# fungsi kuadrat biasa
def kuadrat(x):
    return x**2

# fungsi kuadrat dengan lambda
kuadrat = lambda x: x**2
print(kuadrat(2))

pangkat = lambda num, pow: num**pow
print(pangkat(2,3))


## kegunaan

# sorting untuk list
list_angka = [1,2,3,4,5,6,7,8,9,10]
list_angka.sort(reverse=True)
print(f"sorting descending: {list_angka}")

list = ["haji", "bando", "cinta", "dunia", "y"]
list.sort(key=len)
print(f"sorting berdasarkan panjang karakter: {list}")

# sort pakai lambda
list2 = ["haji", "bando", "cinta", "dunia", "y", "aa", "bb", "cccd", "deeeed", "eed"]
list2.sort(key=lambda nama:len(nama))
print(f"sorting lambda berdasarkan panjang karakter: {list2}")



# anonymous function
# fungsi yang tidak memiliki nama
# fungsi lambda adalah anonymous function
# currying <- Haskell Curry
# currying adalah teknik membuat fungsi baru dari fungsi yang sudah ada
# dengan mengubah beberapa parameter saja
# contoh

def pangkat(n):
    return lambda angka:angka**n

pangkat2 = pangkat(2)
pangkat3 = pangkat(3)
print(f"pangkat 2 dari 5 adalah {pangkat2(5)}")
print(f"pangkat 3 dari 5 adalah {pangkat3(5)}")
print(f"pangkat bebas = {pangkat(5)(2)}")