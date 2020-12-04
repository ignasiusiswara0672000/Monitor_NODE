import paramiko
import time
import math
from getpass import getpass
paswd = getpass()
ip1 = "192.168.100.38"
client1 = paramiko.SSHClient()
client1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client1.connect(ip1, 22, "09011281924049", paswd)
ip2 = "192.168.100.39"
client2 = paramiko.SSHClient()
client2.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client2.connect(ip2, 22, "username", paswd)

def node1_Segitiga(PilihPerhitungan, inAlas, inTinggi, inSisia, inSisib, inSisic):
    connect = client1.get_transport().open_session()
    connect.invoke_shell()
    connect.send('python3 Perhitungan.py\n')
    connect.send(PilihPerhitungan + "\n")
    connect.send(inAlas + "\n" )
    connect.send(inTinggi + "\n")
    connect.send(inSisia + "\n")
    connect.send(inSisib + "\n")
    connect.send(inSisic + "\n")
    time.sleep(1)
    output = connect.recv(65535)
    print(output.decode("ascii"))

def node1_Lingkaran(PilihPerhitungan, inPhi, inJari):
    connect = client1.get_transport().open_session()
    connect.invoke_shell()
    connect.send('python3 Perhitungan.py\n')
    connect.send(PilihPerhitungan + "\n")
    connect.send(inPhi + "\n")
    connect.send(inJari + "\n")
    time.sleep(1)
    output = connect.recv(65535)
    print(output.decode("ascii"))

def node1_Persegi(PilihPerhitungan, inSisi):
    connect = client1.get_transport().open_session()
    connect.invoke_shell()
    connect.send('python3 Perhitungan.py\n')
    connect.send(PilihPerhitungan + "\n")
    connect.send(inSisi + "\n" )
    output = connect.recv(65535)
    print(output.decode("ascii"))

def node2_Segitiga(PilihPerhitungan, inAlas, inTinggi, inSisia, inSisib, inSisic):
    connect = client2.get_transport().open_session()
    connect.invoke_shell()
    connect.send('python3 Perhitungan.py\n')
    connect.send(PilihPerhitungan + "\n")
    connect.send(inAlas + "\n")
    connect.send(inTinggi + "\n")
    connect.send(inSisia + "\n")
    connect.send(inSisib + "\n")
    connect.send(inSisic + "\n")
    time.sleep(1)
    output = connect.recv(65535)
    print(output.decode("ascii"))

def node2_Lingkaran(PilihPerhitungan, inPhi, inJari):
    connect = client2.get_transport().open_session()
    connect.invoke_shell()
    connect.send('python3 Perhitungan.py\n')
    connect.send(PilihPerhitungan + "\n")
    connect.send(inPhi + "\n" )
    connect.send(inJari + "\n")
    time.sleep(1)
    output = connect.recv(65535)
    print(output.decode("ascii"))

def node2_Persegi(PilihPerhitungan, inSisi):
    connect = client2.get_transport().open_session()
    connect.invoke_shell()
    connect.send('python3 Perhitungan.py\n')
    connect.send(PilihPerhitungan + "\n")
    connect.send(inSisi + "\n" )
    output = connect.recv(65535)
    print(output.decode("ascii"))

def PilihNodeSegitiga(PilihPerhitungan, inAlas, inTinggi, inSisia, inSisib, inSisic):
    Pilihan = input("Pemilihan Node\n1. Node 1\n2. Node 2\nPilih Node yang akan melakukan penghitungan : ")
    Pilih = Pilihan.split(",")
    if "1" in Pilih :
        node1_Segitiga(PilihPerhitungan, inAlas, inTinggi, inSisia, inSisib, inSisic)
    if "2" in Pilih :
        node2_Segitiga(PilihPerhitungan, inAlas, inTinggi, inSisia, inSisib, inSisic)
    menu()

def PilihNodeLingkaran(PilihPerhitungan, inPhi, inJari):
    Pilihan = input("Pemilihan Node\n1. Node 1\n2. Node 2\nPilih Node yang akan melakukan penghitungan : ")
    Pilih = Pilihan.split(",")
    if "1" in Pilih :
        node1_Lingkaran(PilihPerhitungan, inPhi, inJari)
    if "2" in Pilih :
        node2_Lingkaran(PilihPerhitungan, inPhi, inJari)
    menu()

def PilihNodePersegi(PilihPerhitungan, inSisi):
    Pilihan = input("Pemilihan Node\n1. Node 1\n2. Node 2\nPilih Node yang akan melakukan penghitungan : ")
    Pilih = Pilihan.split(",")
    if "1" in Pilih:
        node1_Persegi(PilihPerhitungan, inSisi)
    if "2" in Pilih:
        node2_Persegi(PilihPerhitungan, inSisi)
    menu()

def menu():
    print("___________________________________________")
    PilihPerhitungan = input("\nProgram Perhitungan\n1. Hitung Luas dan Keliling Segitiga\n2. Hitung Luas dan Keliling Lingkaran\n3. Hitung Luas dan Keliling Persegi\n4. Keluar\nMasukkan Pilihan : ")
    if PilihPerhitungan == "1" :
        print("\nHitung Luas dan Keliling Segitiga")
        inAlas = str(input("Masukkan Alas : "))
        inTinggi = str(input("Masukkan Tinggi : "))
        inSisia = str(input("Masukkan sisi a : "))
        inSisib = str(input("Masukkan sisi b : "))
        inSisic = str(input("Masukkan sisi c : "))
        PilihNodeSegitiga(PilihPerhitungan, inAlas, inTinggi, inSisia, inSisib, inSisic)
    if PilihPerhitungan == "2" :
        print("\nHitung Luas dan Keliling Lingkaran")
        inPhi = str(math.pi)
        inJari = str(input("Masukkan Jari-jari : "))
        PilihNodeLingkaran(PilihPerhitungan, inPhi, inJari)
    if PilihPerhitungan == "3" :
        print("\nHitung Luas dan Keliling Persegi")
        inSisi = str(input("Masukkan Sisi : "))
        PilihNodePersegi(PilihPerhitungan, inSisi)
    if PilihPerhitungan == "4" :
        print("Program Selesai")

menu()