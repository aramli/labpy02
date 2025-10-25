print("Program untuk mengurutkan data")

# Input bilangan
satu = int(input("Masukan bilangan Ke-1 : "))
dua = int(input("Masukan bilangan Ke-2 : "))
tiga = int(input("Masukan bilangan Ke-3 : "))
empat = int(input("Masukan bilangan Ke-4 : "))

# Simpan ke dalam list
bilangan = [satu, dua, tiga, empat]

# Proses pengurutan manual dengan if
if bilangan[0] > bilangan[1]:
    bilangan[0], bilangan[1] = bilangan[1], bilangan[0]
if bilangan[0] > bilangan[2]:
    bilangan[0], bilangan[2] = bilangan[2], bilangan[0]
if bilangan[0] > bilangan[3]:
    bilangan[0], bilangan[3] = bilangan[3], bilangan[0]
if bilangan[1] > bilangan[2]:
    bilangan[1], bilangan[2] = bilangan[2], bilangan[1]
if bilangan[1] > bilangan[3]:
    bilangan[1], bilangan[3] = bilangan[3], bilangan[1]
if bilangan[2] > bilangan[3]:
    bilangan[2], bilangan[3] = bilangan[3], bilangan[2]

# Tampilkan hasil
print("Urutan Bilangan:", bilangan)
