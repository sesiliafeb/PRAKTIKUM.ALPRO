# BIMILLAH SEMOGA ACC YA ALLAH
ukm = {
    'ukm_PA': ["Budi", "Ani", "Joko"],
    'ukm_badmintoon': ["Joko", "Siti", "Eka", "Rini", "Hadi", "Deni"],
    'ukm_teater': ["Ani", "Dedi", "Fika", "Maya", "Ahmad"],
    'ukm_tari': ["Siti", "Fika", "Gusman"]
}

print("====================| Data Unit Kegiatan Mahasiswa |====================")
for key, value in ukm.items():
    print(key, ":", value)
print()
print("===============================| Pilihan |===============================")
print("Pilihan 1 untuk menampilkan data Mahasiswa yang bergabung di lebih dari satu UKM")
print("Pilihan 2 untuk menambahkan anggota UKM PA (Pecinta Alam)")
print("Pilihan 3 untuk menambahkan anggota UKM badmintoon")
print("Pilihan 4 untuk menghapus nama anggota UKM badmintoon")
print("Pilihan 5 untuk menampilkan anggota UKM dengan kurang dari 4 orang")
print("Pilihan 6 untuk menampilkan data Mahasiswa yang tidak bergabung di UKM mana pun")
print()
print("==========================================================================")

while True:
    pilihan_data = int(input("Masukkan pilihan yang ingin Anda cari: "))


    # Hitung mahasiswa yang bergabung dalam lebih dari satu UKM
    if pilihan_data == 1:
        gabung_lebih_dari_satu = {}
        for nama_ukm, mahasiswa_list in ukm.items():
            for mahasiswa in mahasiswa_list:
                if mahasiswa in gabung_lebih_dari_satu:
                    gabung_lebih_dari_satu[mahasiswa].append(nama_ukm)
                else:
                    gabung_lebih_dari_satu[mahasiswa] = [nama_ukm]
        for mahasiswa, ukm in gabung_lebih_dari_satu.items():
            if len(ukm) > 1:
                print(mahasiswa, "bergabung di UKM:", ukm)
        print()
    
    # Menambahkan anggota UKM PA
    elif pilihan_data == 2:
        nama = input("Masukkan nama anggota baru UKM PA: ")
        ukm['ukm_PA'].append(nama)
        print(ukm['ukm_PA'])
    
    # Menambahkan anggota UKM badmintoon
    elif pilihan_data == 3:
        nama = input("Masukkan nama anggota baru UKM badmintoon: ")
        ukm['ukm_badmintoon'].append(nama)
        print(ukm['ukm_badmintoon'])
        print()

    # Menghapus nama anggota UKM badmintoon
    elif pilihan_data == 4:
        nama = input("Masukkan nama anggota yang ingin dihapus dari UKM badmintoon: ")
        ukm['ukm_badmintoon'].remove(nama)
        print(ukm['ukm_badmintoon'])
        print()
        
    # Menampilkan anggota UKM dengan kurang dari 4 orang
    elif pilihan_data == 5:
        print("UKM dengan anggota kurang dari 4 orang:")
        for ukm_nama, anggota_list in ukm.items():
            if len(anggota_list) < 4:
                print(ukm_nama, ":", anggota_list)
        print()
    
    # Menampilkan data Mahasiswa yang tidak bergabung di UKM mana pun
    elif pilihan_data == 6:
        mahasiswa_tidak_gabung = []
        for mahasiswa in ukm['ukm_PA'] + ukm['ukm_badmintoon'] + ukm['ukm_teater'] + ukm['ukm_tari']:
            if all(mahasiswa not in anggota_list for anggota_list in ukm.values()):
                mahasiswa_tidak_gabung.append(mahasiswa)
        
        print("Mahasiswa yang tidak bergabung di UKM mana pun:", mahasiswa_tidak_gabung)
        print()

    else : 
           print ("Piihan tidak valid silahkan pilih 1/2/3/4/5/6")


    ulang = (input("Apakah anda ingin menampilkan data lagi? y/t :")).lower()
    if ulang == "t" :
        print("Program selesai, Terimakasih hari harinya :) ")

    
        break 

