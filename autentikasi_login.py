akun = {
    "user": "password123",
    "admin":"admin123"
}

def login():
    print("selamat datang di menu login")
    username = input("masukkan usernae: ")
    password = input("masukkan password: ")

    if username in akun and akun[username] == password:
        print(f"selamat datang, {username}.")
    else:
        print("login gagal! username atau pasword salah.")

login()