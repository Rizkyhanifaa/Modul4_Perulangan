
#Range (Max)
for i in range (7):
    print("Hallo World")

print("--------------")

#Range (Min, Max)
for i in range(1, 10):
    print(f"Perulangan ke- {i}")

print("--------------")

#Range (Min, Max, Step)
for i in range(0,20, 2):
    print(f"Step ke- {i}")

print("--------------")

#Perulangan Menurun / Decrement
for i in range(10, 0, -1):
    print(i)

print("--------------")

#Fungsi Break pada Perulangan "for"
#fungsi perulangan break = menghentikan secara paksa
for i in range(1, 10):
    print("Ini Perulangan ke- ", i)
    if i == 7:
        print("Perulangan ke-", i, "dihentikan")
        break
print("--------------")

#Fungsi Continue pada Perulangan "for"
#Fungsi Continue = di skip / dilewati
for i in range(1, 10):
    #Skip jika i == 5
    if (i == 5):
        continue
    print(i)
