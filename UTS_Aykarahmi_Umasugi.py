buku = ["","1.HTML5, harga : 30000 -",
"2. python, harga :20000 -", 
"3. javaScriep, harga : 250000 -", 
"4. Photoshop, harga : 40000 -", 
"5. Php, Harga : 35000 -",
"6. C++, harga : 15000 "]
a=str(input("pililah, jika membeli buku Tuliskan Beli, dan jika masuk ke Admin tuliskan admin :"))
if a == "beli":
    print("selamat datang pada aplikasi  penjualan buku")
    print("----------------------------------------------------------")
    b = input("apakah anda mau membeli buku, tuliskan ya? :")
    if b in ["ya", "YA", "Ya"]:
        print("berikut kami tamilkan judul judul buku sebagai berikut :")
        print("========================================================")
        for x in buku:
            print(x)
        pilih = int(input("masukan nomor buku di atas :"))
        if pilih == 1:
            harga = 30000
            print("buku yang anda beli :",buku[1])
            print("====================================================")
            tanya =str(input("apakah masi beli buku, jika masi masukan nmor buku, jika tidan, tuliskan tidak :"))
            if tanya == "2":
                harga = 50000
                jum = 2
                print("============================================")
                print("di batasi pembelian buku maxsimal dua buku ")
                print("buku yang anda beli ::",buku[1],buku[2])
                print("============================================")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif tanya == "3":
                harga = 50000
                jum = 2
                print("============================================")
                print("di batasi pembelian buku maxsimal dua buku ")
                print("buku yang anda beli ::",buku[1],buku[3])
                print("============================================")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif  tanya == "4":
                harga = 70000
                jum = 2
                print("============================================")
                print("di batasi pembelian buku maxsimal dua buku ")
                print("buku yang anda beli ::",buku[1],buku[4])
                print("============================================")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif tanya == "5":
                harga = 65000
                jum = 2
                print("============================================")
                print("di batasi pembelian buku maxsimal dua buku ")
                print("buku yang anda beli ::",buku[1],buku[5])
                print("============================================")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif tanya == "6":
                harga = 45000
                jum = 2
                print("============================================")
                print("di batasi pembelian buku maxsimal dua buku ")
                print("buku yang anda beli ::",buku[1],buku[6])
                print("============================================")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif tanya == "tidak":
                harga = 30000
                jum = 1
                print("============================================")
                print("buku yang anda beli ::",buku[1])
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)  
        elif pilih == 2:
            harga = 20000
            print("buku yang anda beli :",buku[2])
            print("====================================================")
            tanya =str(input("apakah masi beli buku, jika masi masukan nmor buku, jika tidan, tuliskan tidak :"))
            if tanya == "3":
                harga = 45000
                jum = 2
                print("============================================")
                print("di batasi pembelian buku maxsimal dua buku ")
                print("buku yang anda beli ::",buku[2],buku[3])
                print("============================================")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif tanya == "4":
                harga = 60000
                jum = 2
                print("============================================")
                print("di batasi pembelian buku maxsimal dua buku ")
                print("buku yang anda beli ::",buku[2],buku[4])
                print("============================================")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif  tanya == "5":
                harga = 55000
                jum = 2
                print("============================================")
                print("di batasi pembelian buku maxsimal dua buku ")
                print("buku yang anda beli ::",buku[2],buku[5])
                print("============================================")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif tanya == "6":
                harga = 35000
                jum = 2
                print("============================================")
                print("di batasi pembelian buku maxsimal dua buku ")
                print("buku yang anda beli ::",buku[2],buku[6])
                print("============================================")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif tanya == "1":
                harga = 50000
                jum = 2
                print("============================================")
                print("di batasi pembelian buku maxsimal dua buku ")
                print("buku yang anda beli ::",buku[2],buku[1])
                print("============================================")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif tanya == "tidak":
                harga = 20000
                jum = 1
                print("============================================")
                print("buku yang anda beli ::",buku[2])
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
        elif pilih == 3:
            harga = 25000
            print("buku yang anda beli : ",buku[3])
            print("====================================================")
            tanya =str(input("apakah masi beli buku, jika masi masukan nmor buku, jika tidan, tuliskan tidak :"))
            if tanya == "3":
                harga = 65000
                jum = 2
                print("============================================")
                print("di batasi pembelian buku maxsimal dua buku ")
                print("buku yang anda beli ::",buku[3],buku[4])
                print("============================================")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif tanya == "5":
                harga = 60000
                jum = 2
                print("============================================")
                print("di batasi pembelian buku maxsimal dua buku ")
                print("buku yang anda beli ::",buku[3],buku[5])
                print("============================================")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif  tanya == "6":
                harga = 40000
                jum = 2
                print("============================================")
                print("di batasi pembelian buku maxsimal dua buku ")
                print("buku yang anda beli ::",buku[2],buku[5])
                print("============================================")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif tanya == "1":
                harga = 55000
                jum = 2
                print("============================================")
                print("di batasi pembelian buku maxsimal dua buku ")
                print("buku yang anda beli ::",buku[3],buku[1])
                print("============================================")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif tanya == "2":
                harga = 45000
                jum = 2
                print("============================================")
                print("di batasi pembelian buku maxsimal dua buku ")
                print("buku yang anda beli ::",buku[3],buku[2])
                print("============================================")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif tanya == "tidak":
                harga = 25000
                jum = 1
                print("============================================")
                print("buku yang anda beli ::",buku[3])
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
        elif pilih == 4:
            harga = 40000
            print("buku yang anda beli :",buku[3])
            print("====================================================")
            tanya =str(input("apakah masi beli buku, jika masi masukan nmor buku, jika tidan, tuliskan tidak :"))
            if tanya == "4":
                harga = 35000
                jum = 2
                print("============================================")
                print("di batasi pembelian buku maxsimal dua buku ")
                print("buku yang anda beli ::",buku[4],buku[5])
                print("============================================")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif tanya == "6":
                harga = 55000
                jum = 2
                print("============================================")
                print("di batasi pembelian buku maxsimal dua buku ")
                print("buku yang anda beli ::",buku[4],buku[6])
                print("============================================")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif  tanya == "1":
                harga = 60000
                jum = 2
                print("============================================")
                print("di batasi pembelian buku maxsimal dua buku ")
                print("buku yang anda beli ::",buku[4],buku[1])
                print("============================================")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif tanya == "2":
                harga = 60000
                jum = 2
                print("============================================")
                print("di batasi pembelian buku maxsimal dua buku ")
                print("buku yang anda beli ::",buku[4],buku[2])
                print("============================================")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif tanya == "3":
                harga = 65000
                jum = 2
                print("============================================")
                print("di batasi pembelian buku maxsimal dua buku ")
                print("buku yang anda beli ::",buku[4],buku[3])
                print("============================================")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif tanya == "tidak":
                harga = 40000
                jum = 1
                print("============================================")
                print("buku yang anda beli ::",buku[4])
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
        elif pilih == 5:
            harga = 35000
            print("buku yang anda beli : ",buku[5])
            print("====================================================")
            tanya =str(input("apakah masi beli buku, jika masi masukan nmor buku, jika tidan, tuliskan tidak :"))
            if tanya == "6":
                harga = 50000
                jum = 2
                print("============================================")
                print("di batasi pembelian buku maxsimal dua buku ")
                print("buku yang anda beli ::",buku[5],buku[6])
                print("============================================")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif tanya == "1":
                harga = 65000
                jum = 2
                print("============================================")
                print("di batasi pembelian buku maxsimal dua buku ")
                print("buku yang anda beli ::",buku[5],buku[1])
                print("============================================")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif  tanya == "2":
                harga = 55000
                jum = 2
                print("============================================")
                print("di batasi pembelian buku maxsimal dua buku ")
                print("buku yang anda beli ::",buku[5],buku[2])
                print("============================================")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif tanya == "3":
                harga = 55000
                jum = 2
                print("============================================")
                print("di batasi pembelian buku maxsimal dua buku ")
                print("buku yang anda beli ::",buku[5],buku[3])
                print("============================================")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif tanya == "4":
                harga = 75000
                jum = 2
                print("============================================")
                print("di batasi pembelian buku maxsimal dua buku ")
                print("buku yang anda beli ::",buku[5],buku[4])
                print("============================================")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif tanya == "tidak":
                harga = 35000
                jum = 1
                print("============================================")
                print("buku yang anda beli ::",buku[5])
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
        elif pilih == 6:
            harga = 15000
            print("buku yang anda beli : ",buku[6])
            print("====================================================")
            tanya =str(input("apakah masi beli buku, jika masi masukan nmor buku, jika tidan, tuliskan tidak :"))
            if tanya == "1":
                harga = 45000
                jum = 2
                print("============================================")
                print("di batasi pembelian buku maxsimal dua buku ")
                print("buku yang anda beli ::",buku[6],buku[1])
                print("============================================")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif tanya == "2":
                harga = 45000
                jum = 2
                print("============================================")
                print("di batasi pembelian buku maxsimal dua buku ")
                print("buku yang anda beli ::",buku[6],buku[2])
                print("============================================")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif  tanya == "3":
                harga = 40000
                jum = 2
                print("============================================")
                print("di batasi pembelian buku maxsimal dua buku ")
                print("buku yang anda beli ::",buku[6],buku[3])
                print("============================================")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif tanya == "4":
                harga = 55000
                jum = 2
                print("============================================")
                print("di batasi pembelian buku maxsimal dua buku ")
                print("buku yang anda beli ::",buku[6],buku[4])
                print("============================================")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif tanya == "5":
                harga = 50000
                jum = 2
                print("============================================")
                print("di batasi pembelian buku maxsimal dua buku ")
                print("buku yang anda beli ::",buku[6],buku[5])
                print("============================================")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif tanya == "tidak":
                harga = 15000
                jum = 1
                print("============================================")
                print("buku yang anda beli ::",buku[6])
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            else:
                print("nomor yang anda masukan slah")
        else:
            print("angka yang anda masukan tidak tercantum dalah nomor buku")
            print("silahkan mulai kembali!")
elif a == "admin":
    print("selamat datang admin pada aplikasi penjualan buku")
    print("--------------------------------------------------------------------")
    print("Stok-Stok Buku")
    print(buku)
    print("===================================================================")
    print("jikan menambah tekan 1, jika mengubah tekan 2, dan jika menghapus tekan 3")
    pilih = int(input("masukan pilihan :"))
    if pilih == 1:
        print("anda menambahkan stok buku, dengan format ikuti di bawah ini")
        print("{nomor selanjutnya. nama buku, harga : diisi}")
        stok = str(input("masukan stok : "))
        buku.append(stok)
        print(buku)
    elif pilih == 2:
        print("anda mengubah stok buku")
        ubh = int(input("masukan nomor berapa yang ingin di ubah ? 1, 2, 3, 4, 5, 6:"))
        print("yang akan anda ubah :", buku[ubh])
        print("format pengisian 'nmr, nama, harga ")
        ganti = str(input("masukan nmr, nama buku dan harga buku yang anda gantikan:"))
        buku[ubh]=ganti
        print("anda mengubah buku pertama dengan", ganti)
        print(buku)
    elif pilih == 3:
        print("anda ingin menghapus stok buku")
        hps = int(input("masukan nomor berapa yang ingin anda hapus 1,2,3,4,5, 6 :"))
        if hps == 1:
            del buku[hps]
            print(buku)
        elif hps == 2:
            del buku[hps]
            print(buku)
        elif hps == 3:
            del buku[hps]
            print(buku)
        elif hps == 4:
            del buku[hps]
            print(buku)
        elif hps == 5:
            del buku[hps]
            print(buku)
        elif hps == 6:
            del buku[hps]
            print(buku)
        else:
            print("anda masuka nomor yang tidak tersedia!")
            print("silahkan login kembali !")