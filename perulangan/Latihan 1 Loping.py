# Loop baris dari 0 - 9
for baris in range(10):
    # Tentukan awal dan akhir untuk setiap baris
    awal = baris
    akhir = awal + 10
    # Cetak angka dari awal sampai akhir
    for angka in range(awal, akhir):
        print(angka, end='   ')
    print()  # Untuk Pindah ke baris baru
