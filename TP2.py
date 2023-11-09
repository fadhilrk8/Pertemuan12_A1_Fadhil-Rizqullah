import math
# Mencetak Menu
def menu():
    print("Pilih Bentuk 2D")
    print()
    print("1. Persegi Panjang")
    print("2. Lingkaran")
    print("3. Segitiga")
    print("4. Keluar")

def luas_persegi_panjang(p,l):
    return p*l

def luas_lingkaran(r):
    return math.pi*r**2

def luas_segitiga(a,t):
    return (a*t)/2
    
while True:
    menu()
    pilihan = int(input("Masukkan pilihan anda: "))
    print()
# Menghitung luas Persegi Panjang
    if pilihan == 1:
        print("Menghitung Luas Persegi Panjang")
        p = float(input("Masukkan Panjang : "))
        l = float(input("Masukkan Lebar : "))
        luas = p * l
        print("Luas Persegi Panjang adalah", luas)
        print()
        print("Coba lagi [Y/N]? ")
        back = input().upper()
        if back == "Y":
            menu()
        else:
            exit()

    # Menghitung Luas Lingkaran
    elif pilihan == 2:
        print("Menghitung Luas Lingkaran")
        r = float(input("Masukkan Jari-Jari : "))
        luas = 3.14 * (r ** 2)
        print("Luas Lingkaran adalah", luas)
        print()
        print("Coba lagi [Y/N]? ")
        back = input().upper()
        if back == "Y":
            menu()
        else:
            print("Suwun")
            exit()

    # Menghitung Luas Segitiga
    elif pilihan == 3:
        print("Menghitung Luas Segitiga")
        a = float(input("Masukkan Alas : "))
        t = float(input("Masukkan Tinggi : "))
        luas = (a * t) / 2
        print("Luas Segitiga adalah", luas)
        print()
        print("Coba lagi [Y/N]? ")
        back = input().upper()
        if back == "Y":
            menu()
        else:
            exit()

    elif pilihan == 4:
        exit()
    else:
        print("Pilihan tidak tersedia")

    # Program Utama
    def main():
        menu()

    if __name__ == "__main__":
        main()
