#      =====UAS BANGUN DATAR=====

def luaspersegi(sisi):
    return sisi * sisi
    
def kelilingpersegi(sisi):
    return 4 * sisi

def luaspersegipanjang(panjang, lebar):
    return panjang * lebar

def kelilingpersegipanjang(panjang, lebar):
    return 2 * (panjang + lebar)

def luasjajargenjang(alas, tinggi):
    return alas * tinggi
def kelilingjajargenjang(sisi_miring, alas):
    return  2 * (sisi_miring + alas)

def luaslingkaran(r):
    return 3.14 * r * r
def kelilinglingkaran(r):
    return 2 * 3.14 * r

#              =====INPUT NAMA=====

print("============================================")
nama = input("Masukkan nama anda: ")

print(nama, ", Selamat Datang di Aplikasi Program Bangun Datar!")

#            =====MENU PILIHAN=====

print("Pilihlah Bangun Datar?: ")
daftar_bangun_datar = ["1. persegi,  2. persegi panjang, 3. jajar genjang, 4. lingkaran"]
i = 0

while i < len(daftar_bangun_datar):
    print(daftar_bangun_datar[i])
    i += 1

    pilihan = int(input("Masukkan Pilihan Anda (1-4): "))

#              ======LOGIKA PROGRAM=====

while True:
        if pilihan == 1:
            sisi = int(input("masukkan sisi persegi: "))
            print("Luas Persegi adalah:", luaspersegi(sisi))
            print("Keliling Persegi:", kelilingpersegi(sisi))

        elif pilihan == 2:
            panjang = int(input("masukkan panjang persegi panjang: "))
            lebar = int(input("masukkan lebar persegi panjang: "))
            print("Luas persegi panjang adalah:", luaspersegipanjang(panjang,lebar))
            print("Keliling persegi panjang adalah:", kelilingpersegipanjang(panjang,lebar))

        elif pilihan == 3:
            alas  = int(input("masukkan alas jajar genjang: "))
            tinggi = int(input("masukkan tinggi jajar genjang:" ))
            sisi = int(input("masukkan sisi jajar genjang:" ))
            print("Luas jajar genjang:", luasjajargenjang(alas, tinggi))
            print("Keliling jajar genjang:", kelilingjajargenjang(sisi, alas))

        elif pilihan == 4:
            r = int(input("masukkan jari-jari lingkaran:" ))
            print("luas lingkaran adalah:", luaslingkaran(r))
            print("keliling lingkaran adalah:", kelilinglingkaran(r))

        else:
            print("Pilihan tidak tersedia")

        ulang = input("Apakah anda ingin menghitung lagi? (ya/tidak): ")
        if(ulang == "ya"):
            print("Silahkan jalankan Ulang program ini!")
            continue
        else:
            print("Terima Kasih", nama)
            print("PROGRAM SELESAI.")
            break