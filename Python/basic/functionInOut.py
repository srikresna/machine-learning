def ubah(list_saya):
    "Deklarasi Variabel list_saya berikut hanya dikenali (berlaku) di dalam fungsi ubah"
    list_saya = [1, 2, 3, 4] 
    print ('Nilai di dalam fungsi: {}'.format(list_saya))
 
# Panggil fungsi ubah
list_saya = [10, 20, 30]
ubah(list_saya)
print('Nilai di luar fungsi: {}'.format(list_saya))