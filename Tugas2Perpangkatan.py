
print("=== PROGRAM SEDERHANA MENGHITUNG PANGKAT ===")
n = int(input("Masukkan Bilangan = "))
p = int(input("Masukkan Pencacah = "))

hasil = n

for i in range(p - 1):
    hasil *= n
    print("Hasil Pangkat = ", hasil)
