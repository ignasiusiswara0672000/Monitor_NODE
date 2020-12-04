def Pilih():
    Pilihan =  input()
    if Pilihan == "1":
        Segitiga()
    elif Pilihan == "2":
        Lingkaran()
    elif Pilihan == "3":
        Persegi()

def Segitiga():
    inAlas = float(input())
    inTinggi = float(input())
    inSisia = float(input())
    inSisib = float(input())
    inSisic = float(input())
    Luas = 0.5 * inAlas * inTinggi
    Keliling = inSisia + inSisib + inSisic
    print("\nNilai diambil dari Node ke-1")
    print("Luas Segitiga\t\t:", Luas)
    print("Keliling Segitiga\t:", Keliling)

def Lingkaran():
    inPhi = float(input())
    inJari = float(input())
    Luas = inPhi * (inJari*inJari)
    Keliling = 2 * inPhi * inJari
    print("\nNilai diambil dari Node ke-1")
    print("Luas Lingkaran\t\t:", Luas)
    print("Keliling Lingkaran\t:", Keliling)

def Persegi():
    inSisi = float(input())
    Luas = inSisi * inSisi
    Keliling = 4 * inSisi
    print("\nNilai diambil dari Node ke-1")
    print("Luas Persegi\t\t:", Luas)
    print("Keliling Persegi\t:", Keliling)

Pilih()