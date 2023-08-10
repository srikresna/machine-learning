import copy
# dummy data
a = ["Rijal", "Fadila", "Anan"]
b = a
print(f"Data a: {a}")

# kita akan merubah member dari a

a[0] = "Rizal"
b.sort
print(f"Data a: {a}")
print(f"Data b: {b}")

# address dari a dan b sama
print(f"Address a: {hex(id(a))}")
print(f"Address b: {hex(id(b))}")

# coba menggunakan deepcopy
c = copy.deepcopy(a)
print(f"Data c: {c}")

# check address 
print(f"Address a", hex(id(a)))
print(f"Address c", hex(id(c)))

# test
c = a.copy()
a[0] = "NABDO"
print(f"Data a: {a}")
print(f"Data c: {c}")

