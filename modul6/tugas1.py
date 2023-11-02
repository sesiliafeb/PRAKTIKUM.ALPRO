# BISMILLAH LANGSUNG ACC YA ALLAH. AAMIIN

biodata = {
    'Nama' : 'Susanti',
    'Alamat' : 'Surakarta',
    'Prodi' : 'Sistem Informasi',
    'Semester' : '5',
    'Angkatan' : '2015'
}

biodata ['Nama'] = input("masukkan Nama :")
biodata ['Alamat'] = input("masukkan Alamat :")
biodata ['Prodi'] = input("masukkan Prodi :")
tahun_pindah = int(input("masukkan tahun pindah :"))
print()

print("Pada tahun", tahun_pindah, 
            biodata ['Nama'], "pindah tempat tinggal di", 
            biodata ['Alamat'], "pada saat itu juga", 
            biodata ['Nama'], "pindah Prodi",
            biodata ['Prodi'],)
print()

while True :
    tahun_berhenti = (input("Apakah beliau berhenti kuliah? ya/tidak :")).lower()
    print()
    if tahun_berhenti == 'tidak' :
        break
     
    elif tahun_berhenti == 'ya' : 
        tahun_berhenti = int(input("masukkan tahun berhenti :"))
        print ("Namun pada tahun", tahun_berhenti, biodata ['Nama'], 
                "memutuskan untuk berhenti kuliah")
        print()
        break 
      
    else : 
        print("Pilihan tidak valid. Silahkan pilih ya/tidak").lower()
        print()
print("Program selesai, Terimakasih")
     
       
