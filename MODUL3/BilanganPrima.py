#menentukan bilangan prima
  
angka = int(input("masukan angka: ")) 
prima = "adalah bilangan prima"

if (angka == 1 or angka == 0): #jika dimasukan angka 1 atau 0 program akan memunculkan bukan bilangan prima
    prima = "bukan bilangan prima"
for i in range (2, angka): #range u/menampilkan deret angka
    if (angka % i == 0): #hasil sisa bagi = 0 bukan bilangan prima
        prima = "bukan bilangan prima"
print (angka, prima)
