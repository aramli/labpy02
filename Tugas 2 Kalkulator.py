print("Program Kalkulator sederhana")
print("-----------------------------------")

bil_1 =int(input("inputkan bilangan pertama : "))
bil_2 =int(input("inputkan bilangan kedua : "))

pilihan = """
-----------------------------------
Pilih operasi bilangan
1. Tambah (+)
2. Kurang (-)
3. Kali   (x)
4. Bagi   (/)
-----------------------------------
"""
print(pilihan)

operator =input("pilih operasi yang akan dilakukan : ")

if operator == "1" :
	hasil =bil_1+bil_2
elif operator == "2" :
	hasil =bil_1-bil_2
elif operator == "3" :
	hasil =bil_1*bil_2
elif operator == "4" :
	hasil =bil_1/bil_2
else :
    hasil = "operasi gagal. Anda belum pilih operasi bilangan"
print ("hasil dari operasi adalah : ",hasil)
