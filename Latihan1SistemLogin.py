

print("===== SISTEM LOGIN SEDERHANA =====")
login = 0
while True:
    username = input("Masukkan username : ")
    password = input("Masukkan password : ")

    if login == 3:
        print("Login gagal ! Kesempatan mencoba sudah hanis. Silahkan coba lagi nanti")
        break

    if username == "hanifa" and password == "123":
        print("Selamat datang ", username, "!")
        break

    else:
        print("Coba cek kembali, username atau password salah !")
        login += 1