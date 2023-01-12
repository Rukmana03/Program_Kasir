print("=========TOKO SUKA KRIPIK==========")
pembeli = input("Nama Pembeli: ")

def kripik():
    global totalkripik
    global pcs
    global kripik
    print("\n==========ANEKA KRIPIK===========")
    print("1. Kripik Singkong - Rp.5000,00")
    print("2. Kripik Talas - Rp.6000,00")
    print("3. Kripik Kentang - Rp.7000,00")
    opt = int(input("masukkan pilihan 1/2/3 : "))
    pcs = int(input("masukkan pcs : "))

    if opt == 1:
        totalkripik = pcs * 5000
        print(pcs, "Kripik Singkong - Rp.", totalkripik)
        kripik = ("Kripik Singkong")
    elif opt == 2:
        totalkripik = pcs * 6000
        print(pcs, "Kripik Talas - Rp.", totalkripik)
        kripik = ("Kripik Talas")
    elif opt == 3:
        totalkripik = pcs * 7000
        print(pcs, "Kripik Kentang - Rp.", totalkripik)
        kripik = ("Kripik Kentang")
    else:
        print("Pilihan anda tidak ada dalam daftar menu\nSilahkan pilih kembali!!")
        kripik()

def minuman():
    global totalminuman
    global gelas
    global minum
    print("\n==========MENU MINUMAN==========")
    print("1. Kopi susu - Rp.4000,00")
    print("2. Teh Pucuk - Rp.3000,00")
    print("3. Teh Botol - Rp.5000,00")
    fx = int(input("masukkan pilihan 1/2/3 : "))
    gelas = int(input("masukan pcs : "))

    if fx == 1:
        totalminuman = gelas * 4000
        print(gelas, "Susu Kopi - Rp.", totalminuman)
        minum = ("Kopi susu")
    elif fx == 2:
        totalminuman = gelas * 3000
        print(gelas, "Teh Pucuk - Rp.", totalminuman)
        minum = ("Teh Pucuk")
    elif fx == 3:
        totalminuman = gelas * 5000
        print(gelas, "Teh Botol - Rp.", totalminuman)
        minum = ("Teh Botol")
    else:
        print("Pilihan anda tidak ada dalam daftar menu\nSilahkan pilih kembali!!")
        minuman()

kripik()
minuman()
total_semua = totalkripik + totalminuman

print("\nTotal yang harus anda bayar : Rp.", total_semua)
uang = int(input("masukkan uang anda : RP."))
kembalian = int(uang - total_semua)
print("kembalian : ", kembalian)

f = open("nota.txt","w")
f.write("==========S T R U K P E M B E L I A N==========" + "\n")
f.write("Nama : " + (pembeli) + "\n")
f.write("Beli : " + str(pcs) + str(kripik) + "(Rp." + str(totalkripik) + ")" + "\n")
f.write("Beli : " + str(gelas) + str(minum) + "(Rp." + str(totalminuman) + ")" + "\n")
f.write("Tagihan : Rp." + str(total_semua) + "\n")
f.write("Dibayar : Rp." + str(uang) + "\n")
f.write("Kembalian : Rp." + str(kembalian) + "\n")
f.write("===============================================" + "\n")
f.close()

print("nota telah disimpan")