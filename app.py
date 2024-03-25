#hitung luas segitiga
def luas_segitiga():
    a = int(input("Masukkan alas segitiga: "))
    t = int(input("Masukkan tinggi segitiga: "))
    luas = a * t / 2
    print("Luas segitiga adalah: ", luas)
luas_segitiga()

#hitung luas persegi panjang
def luas_persegi_panjang():
    p = int(input("Masukkan panjang persegi: "))
    l = int(input("Masukkan lebar persegi: "))
    luas = p * l
    print("Luas persegi adalah: ", luas)
luas_persegi_panjang()

#hitung luas lingkaran
def luas_lingkaran():
    r = int(input("Masukkan jari-jari lingkaran: "))
    luas = 3.14 * r * r
    print("Luas Lingkaran adalah: ", luas)
luas_lingkaran()
