data0 = [1, 2]
data1 = [3, 4]

data_list_biasa = [1, 2, 3 ,4]

print(f"Data list biasa: {data_list_biasa}")

list_2d = [data0, data1]
import copy
print(f"Data list 2d: {list_2d}")

# bisa ditambahkan data biasa

list_2d.append(5)

data_baru_list_2d = [6, 7]
list_2d.append(data_baru_list_2d)

data_baru2_list_2d = [8, 9, "SARDO"]
list_2d.extend(data_baru2_list_2d)
print(f"Data list 2d: {list_2d}")

# mengakses data list 2d
print(f"Data list 2d: {list_2d}")
print(f"Data list 2d baris 1 kolom 1: {list_2d[0][0]}")
print(f"Data list 2d baris 1 kolom 2: {list_2d[0][1]}")
print(f"Data list 2d baris 2 kolom 1: {list_2d[1][0]}")
print(f"Data list 2d baris 2 kolom 2: {list_2d[1][1]}")

# mengubah elemen list 2d
list_2d[0][0] = 10
print(f"Data list 2d: {list_2d}")



# deepcopy nested list
list_2d_copy = copy.deepcopy(list_2d)

# test ubah data
list_2d[0][0] = 100
print(f"Data list 2d: {list_2d}")
print(f"Data list 2d copy: {list_2d_copy}")

# address
print(f"Address list 2d: {hex(id(list_2d))}")
print(f"Address list 2d copy: {hex(id(list_2d_copy))}")

print("-"*30)
# buat data baru untuk looping list dan enumerate
a = ["Shando", "RUdi", "Rijal", "Fadila", "Anan"]

# looping biasa
print("Looping biasa")
for i in a:
    print(i)

# looping enumerate
print("Looping enumerate")
for i, j in enumerate(a):
    print(f"Index: {i}, Value: {j}")

# looping enumerate dengan start
print("Looping enumerate dengan start")
for i, j in enumerate(a, start=1):
    print(f"Index: {i}, Value: {j}")

# looping enumerate dengan start dan end
print("Looping enumerate dengan start dan end")
for i, j in enumerate(a, start=1):
    if i == 3:
        print("Looping berhenti di index ke 3")
        break
    print(f"Index: {i}, Value: {j}")

# for loop dan range
print("For loop dan range")
for i in range(1, 10):
    print(i)

# while loop
print("While loop")
i = 1
while i < 10:
    print(i)
    i += 1

# list comprehentsion
print("List comprehentsion a + 2")
a = [1, 2, 3, 4, 5]
print(a)
[print(i+2) for i in a]


# for dan if
print("For dan if a + 2 jika genap")
a = [1, 2, 3, 4, 5]
print(a)
[print(i+2) for i in a if i % 2 == 0]

# for dan if else
print("For dan if else a + 2 jika genap, a + 1 jika ganjil")
a = [1, 2, 3, 4, 5]
print(a)
[print(i+2) if i % 2 == 0 else print(i+1) for i in a]
