"""
Created on Fry Jul  7 15:50:33 2021
UAS ALGORITMA PEMROGRAMAN – SMT
 ~ PERHITUNGAN GAJI KARYAWAN CV. LOGOS ~

@author: Indrian Wahyu Kusumawati - 20083000017
"""
#Menampilkan Waktu
import datetime
waktu = datetime.datetime.now()



#Ulang Program
JawabUlang = "y"
while JawabUlang=="y" or JawabUlang=="Y":
    print("======================================================")
    print("                       CV. LOGOS ")
    print("               PERHITUNGAN GAJI KARYAWAN ")
    print("")
    print("Tanggal : " , waktu)
    print("=====================================================")
    print("")

    #Nilai Awal
    KdGolongan = [1,2,3]
    GajiPokok = [2500000, 4500000, 6500000]
    TunjanganIstri = [0.01, 0.03, 0.05]
    TunjanganAnak = 0.02
    BiayaJabatan = 0.0005
    KdJKel =[1,2]
    JnsKel = ['Laki - Laki','Perempuan']
    KdStatusKawin =[1,2]
    StsKwn = ['Kawin','Belum Kawin']
    KdStatusAnak =[1,2]
    StatusAnak = ['Punya Anak','Belum Punya Anak']
    IuranPensiun = 15500
    IuranOrganisasi = 3500

    #Input Nama Karyawan
    NamaKary = input("> Nama Karyawan        : ")

    idx = 0
    while idx < 4:
        
        #Input Golongan
        print("______________________________________________")
        print("             PILIHAN GOLONGAN")
        print("      1. Golongan 1      Rp 2.500.000")
        print("      2. Golongan 2      Rp 4.500.000")
        print("      3. Golongan 3      Rp 6.500.000")
        print("______________________________________________")
        Golongan = int(input("> Kode Golongan        : "))
        
        idx = Golongan

        if idx <= len (KdGolongan) :
            x = 0
            while x<len(KdGolongan):
                if KdGolongan[x] == idx:
                    Gapok = GajiPokok[x]
                x+=1
        else :
            break

        #Input Jenis Kelamin
        print("______________________________________________")
        print("             PILIHAN JENIS KELAMIN")
        print("        1. Laki - Laki      2. Perempuan")
        print("______________________________________________")
        JenisKelamin = int(input("> Kode Jenis Kelamin   : "))
        
        iptJK = JenisKelamin

        if iptJK <= len(KdJKel) :
            x = 0
            while x<len(KdJKel):
                if KdJKel[x] == iptJK:
                    pilihJK = JnsKel[x]
                x+=1
        else :
            break

        #Input Status Kawin
        print("______________________________________________")
        print("             PILIHAN STATUS KAWIN")
        print("         1. Kawin      2. Belum Kawin")
        print("______________________________________________")
        StatusKawin = int(input("> Kode Status Kawin    : "))
        
        iptStsKwn = StatusKawin

        if iptStsKwn <= len(KdStatusKawin) :
            x = 0
            while x<len(KdStatusKawin):
                if KdStatusKawin[x] == iptStsKwn:
                    pilihSK = StsKwn[x]
                x+=1
        else :
            break
        
        #Jika Pilihan Kawin
        if pilihSK == 'Kawin' :
            
            print("______________________________________________")
            print("             PILIHAN STATUS ANAK")
            print("    1. Punya Anak      2. Belum Punya Anak")
            print("______________________________________________")
            StsAnk = int(input("> Kode Status Anak     : "))
            
            iptSA = StsAnk

            if iptSA <= len(KdStatusAnak) :
                x = 0
                while x<len(KdStatusAnak):
                    if KdStatusAnak[x] == iptSA:
                        pilihSA = StatusAnak[x]
                    x+=1
            else :
                break

        #Perhitungan Tunjangan Istri
        if pilihJK == 'Laki - Laki' and pilihSK == 'Kawin' :
            x = 0
            while x < len(KdGolongan):
                if KdGolongan[x] == idx:
                    DptTunjanganIstri = TunjanganIstri[x]
                    totalTunjanganIstri = Gapok * DptTunjanganIstri
                x += 1
        else :
            totalTunjanganIstri = 0

        #Perhitungan Tunjangan Anak
        if pilihSK == 'Kawin' and pilihSA == 'Punya Anak' :
            totalTunjanganAnak = Gapok * TunjanganAnak
        else :
            totalTunjanganAnak = 0
        
        #Perhitungan Gaji Bruto
        GajiBruto = Gapok + totalTunjanganAnak + totalTunjanganIstri

        #Perhitungan Biaya Jabatan
        biayaJabatan = GajiBruto * BiayaJabatan

        #Perhitungan Gaji Netto
        GajiNetto = GajiBruto - biayaJabatan - IuranPensiun - IuranOrganisasi

        
        print("=====================================================")
        print("                  SLIP GAJI KARYAWAN")
        print("                       CV.LOGOS")
        print("Tanggal : " , waktu)
        print("=====================================================")
        print("Nama Karyawan            : " + NamaKary)
        print("Golongan                 : " + str(Golongan))
        print("Jenis Kelamin            : " + pilihJK)
        print("Staus Kawin              : " + pilihSK)
        print("Gaji Pokok               : Rp " + format(Gapok,',.2f'))
        print("Tunjangan Istri          : Rp " + format(totalTunjanganIstri,',.2f'))
        print("Tunjangan Anak           : Rp " + format(totalTunjanganAnak,',.2f'))
        print(">> Gaji bruto            : Rp " + format(GajiBruto,',.2f'))
        print("_____________________________________________________")
        print("Biaya Jabatan            : Rp " + format(biayaJabatan,',.2f'))
        print("Iuran Pensiun            : Rp " + format(IuranPensiun,',.2f'))
        print("Iuran Organisasi         : Rp " + format(IuranOrganisasi,',.2f'))
        print(">>> Gaji Netto           : Rp " + format(GajiNetto,',.2f'))

        print("")

        
        #Inputan untuk break
        JawabUlang = input(">>>> Apakah Anda Ingin Cek Ulang Gaji? (y/t) : ")
        if JawabUlang== "t" or JawabUlang =="T":
            break

#Cetak Notepad
file=open("SLIP GAJI CV LOGOS.txt","w+")
file.write("=====================================================\r")
file.write("                     SLIP GAJI KARYAWAN \r")
file.write("                         CV.LOGOS\r")
file.write("Tanggal : " + format(waktu) + "\r")
file.write("=====================================================\r")
file.write("Nama Karyawan            : " + NamaKary + "\r")
file.write("Golongan                 : " + str(Golongan) + "\r")
file.write("Jenis Kelamin            : " + pilihJK + "\r")
file.write("Status Kawin             : " + pilihSK + "\r")
file.write("Gaji Pokok               : Rp " + format(Gapok,',.2f') + "\r")
file.write("Tunjangan Istri          : Rp " + format(totalTunjanganIstri,',.2f') + "\r")
file.write("Tunjangan Anak           : Rp " + format(totalTunjanganAnak,',.2f') + "\r")
file.write(">> Gaji Bruto            : Rp " + format(GajiBruto,',.2f') + "\r")
file.write("_____________________________________________________\r")
file.write("Biaya Jabatan            : Rp " + format(biayaJabatan,',.2f') + "\r")
file.write("Iuran Pensiun            : Rp " + format(IuranPensiun,',.2f') + "\r")
file.write("Iuran Organisasi         : Rp " + format(IuranOrganisasi,',.2f') + "\r")
file.write(">> Gaji Netto            : Rp " + format(GajiNetto,',.2f') + "\r")
file.write("\r")
file.write("                                 TTD \r")
file.write("                                 MANAJER HRD CV. LOGOS \r")
