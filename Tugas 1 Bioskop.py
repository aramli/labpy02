# Deklarasi harga tiket
T_VIP = 100000
T_REG = 50000

print("Program Pembelian Tiket Bioskop")
print("-. Harga Tiket VIP = Rp.100.000")
print("-. Harga Tiket Regular = Rp.50.000")
print("-----------------------------------")

# Input tiket yang dipesan
print("Silahkan pilih tiket bioskop (VIP = V atau Reguler = R)")
order = input("Tiket pilihan V / R  :").upper()
member =(False,True)[str(input("Apakah punya member ? [YA = Y] atau [TIDAK = T] :").upper())== "Y"]
jumlah = int(input("Berapa jumlah tiket yang akan dibeli? :"))

# Gunakan operator ternary untuk menentukan harga dan jenis tiket
tiket = T_VIP if order == 'V' else T_REG
det = "VIP" if order == 'V' else "REGULAR"

# Hitung diskon jika member, gunakan ternary juga
diskon = (tiket * 0.2) if member else 0
total = (jumlah * tiket) - (jumlah * diskon)

# Output
print("Anda memesan tiket", det)
print("Dengan jumlah", jumlah, "tiket")
print("Total harga yang harus dibayar Rp.", int(total))
