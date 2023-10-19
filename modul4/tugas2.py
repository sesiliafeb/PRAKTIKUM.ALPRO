# program dinamis
def faktorial(n) :
    if n == 0:
        return 1
    else :
        return n * faktorial(n-1)
    
# Input bilangan     
nilai = int(input("masukan nilai :"))

# Memanggil fungsi faktorial dan mencetak hasilnya
hasil = faktorial(nilai)
print ("hasil faktorial :", hasil)


# # program statis
# def faktorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * faktorial(n-1)
    
# nilai = 10

# hasil = faktorial(nilai)
# print("hasil faktorial :", hasil)


