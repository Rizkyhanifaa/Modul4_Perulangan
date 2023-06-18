i = 0
while i <= 7:
    print("Hallo World")
    i += 1

print("--------------")

#Perulangan Increment
# batas akhir selalu dikurang 1 (otomatis)
a = 1
b = 10
while a < b:
    print("Step ke- ", a)
    a += 1

print("--------------")

#Perulangan Decrement
print("Perulangan Decrement")
a = 10
b = 0
while a > b :
    print("Kuota internet anda sisa", a, "GB")
    a -= 1

print("--------------")

#Fungsi Break pada Perulangan "while"
#Fungsi perulangan break = menghentikan secara paksa
a = 0
while True:
    print("Step ke- ",a, "!")
    a += 1
    if a == 7:
        print("Step ke-", a, "dihentikan !")
        break

print("--------------")

#Fungsi Continue pada Perulangan "While"
#Fungsi Continue = di skip / dilewati

angka = ['1','2','3','4','5','6','7','8','9','10']
# skip jika i = bilangan genap
# dan i lebih dari 0
i = -1
while i < len(angka):
    i += 1
    if i % 2 == 0 and i > 0:
        print('skip')
        continue

    # tidak dieksekusi jika continue dipanggil
    print(angka[i])
