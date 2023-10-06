#rata rata nilai 

nama =  (input("masukan nama :"))
nilai_tugas = int (input ("masukan nilai tugas :"))
nilai_uts = int (input("masukan nilai uts :"))
nilai_uas = int(input("masukan nilai uas :"))
nilai_tugas_akhir = int (input("masukan nilai tugas akhir :"))

rata = (nilai_tugas + nilai_uts + nilai_uas + nilai_tugas_akhir)/4

print ("nama :", nama)
print ("nilai rata rata anda adalah :", rata)

if  80 <= rata <= 100 :
    print ("A")
elif 70 <= rata < 79 :
    print ("B")
elif 60 <= rata < 69 :
    print ("C")
elif 40 <= rata < 59  :
    print ("C")
elif  0 <= rata < 40  :
    print("E")
else :
    print("hasil tidak valid")

