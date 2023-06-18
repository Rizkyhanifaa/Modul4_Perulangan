
print("==== PROGRAM SEDERHANA MENGHITUNG JUMLAH TOTAL BILANGAN ====")
n = int(input("Masukkan bilangan = "))
total = 0

# Tampilkan hasil perhitungan
print("Total Nilai =", end=" ")
for i in range(n, 0, -1):
    total += i
    print( i, end=" ")
    if i != 1:
        print(" + ", end="")
print(" = {}".format(total))