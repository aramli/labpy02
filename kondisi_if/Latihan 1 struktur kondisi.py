# Input bilangan
print("program menentukan bilangan terbesar")
satu = int(input("Masukan bilangan Ke-1 : "))
dua = int(input("Masukan bilangan Ke-2 : "))
tiga = int(input("Masukan bilangan Ke-3 : "))
empat = int(input("Masukan bilangan Ke-4 : "))

# Menentukan bilangan terbesar
if satu >= dua and satu >= tiga and satu >= empat:
    terbesar = satu
elif dua >= satu and dua >= tiga and dua >= empat:
    terbesar = dua
elif tiga >= satu and tiga >= dua and tiga >= empat:
    terbesar = tiga
else:
    terbesar = empat

print("Bilangan Terbesar adalah =", terbesar)
