import datetime

mahasiswa1 = {
    'nama': 'Rizal',
    'nim': '20190140000',
    'sks_lulus': 130,
    'beasiswa': False,
    'lahir': datetime.datetime(2000, 1, 1),
}

mahasiswa2 = {
    'nama': 'Candra',
    'nim': '20190140001',
    'sks_lulus': 130,
    'beasiswa': True,
    'lahir': datetime.datetime(2000, 1, 2),
}

mahasiswa3 = {
    'nama': 'Rizky',
    'nim': '20190140002',
    'sks_lulus': 130,
    'beasiswa': False,
    'lahir': datetime.datetime(2000, 1, 3),
}

data_mahasiswa = {
    'key1':mahasiswa1,
    'key2':mahasiswa2,
    'key3':mahasiswa3,
}

print(f"{'KEY':<5}{'NAMA':<10}{'NIM':<15}{'SKS':<5}{'BEASISWA':<10}{'LAHIR':<10}")
print("-"*60)

for mahasiswa in data_mahasiswa:
    KEY = mahasiswa
    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['nim']
    SKS = data_mahasiswa[KEY]['sks_lulus']
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%d-%m-%Y")

    print(f"{KEY:<5}{NAMA:<10}{NIM:<15}{SKS:<5}{BEASISWA:^10}{LAHIR:<10}")

