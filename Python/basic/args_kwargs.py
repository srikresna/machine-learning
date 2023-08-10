'''*args'''

# fungsi biasa
def fungsi(nama, tinggi, berat):
    print(f"Nama saya {nama}, tinggi saya {tinggi} cm, berat saya {berat} kg")


def fungsi_list(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"Nama saya {nama}, tinggi saya {tinggi} cm, berat saya {berat} kg")

print("Fungsi dengan list")
fungsi_list(['Rizal', 170, 70])
print("-"*50)

# memasukkan argumen tanpa batas
def fungsi_dengan_args(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"Nama saya {nama}, tinggi saya {tinggi} cm, berat saya {berat} kg")

print("Fungsi dengan args")
fungsi_dengan_args('Rizal', 170, 70)

def fungsi_dengan_args2(*data):
    # data tipenya tuple
    output = 0
    for angka in data:
        output += angka
    
    return output

print("Fungsi dengan args2")
print(fungsi_dengan_args2(1,2,3,4,5,6,7,8,9,10))
print("-"*50)


# memasukkan argumen tanpa batas dengan batasan
def fungsi_dengan_args_batas(*args):
    print(args[0:5])

print("Fungsi dengan args batas")
print("Kita akan memasukkan 10 angka, tapi hanya 5 angka pertama yang akan ditampilkan")
fungsi_dengan_args_batas(1,2,3,4,5,6,7,8,9,10)


print("-"*50)

'''**kwargs'''
def fungsi_dengan_kwargs(**kwargs):
    nama = kwargs['nama']
    tinggi = kwargs['tinggi']
    berat = kwargs['berat']
    print(f"Nama saya {nama}, tinggi saya {tinggi} cm, berat saya {berat} kg")

print("Fungsi dengan kwargs")
print("Kita akan memasukkan nama, tinggi, dan berat")
fungsi_dengan_kwargs(nama='Rizal', tinggi=170, berat=70)

# gabungan
print("-"*50)
def math(*args, **kwargs):
    output = 0
    for angka in args:
        output += angka
    
    for key, value in kwargs.items():
        print(f"{key} = {value}")
    
    return output

print("Fungsi dengan args dan kwargs")
print("Kita akan memasukkan 10 angka")
print("Kita juga akan memasukkan nama, tinggi, dan berat")
print(math(1,2,3,4,5,6,7,8,9,10, nama='Rizal', tinggi=170, berat=70))