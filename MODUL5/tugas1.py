# #program data makanan

 
# makanan = []
# harga = []
# while True :
#         for i in range(5) : 
#             nama_makanan : input(f"{i+1}. masukkan nama makanan:")
#             makanan.append(makanan)

#             harga_makanan = float(input("masukkan harga :"))
#             harga.append(harga_makanan)

#         print("\ndata makanan :")
#         for i in range(5) :
#             print(f"{i+1} {makanan[i]} - Rp{harga[i]:,.2f}")

#         jawaban = input ("apakah ingin melanjutkan?(yes/no)")
        
#         if jawaban == "no" :
#             break

# list_menu = []
# list_harga = []
# while True :
#     print ("masukkan menu")
#     makanan = input("masukkan nama makanan :")
#     menu = [makanan]
#     list_menu.append(menu)

#     harga_menu = float(input(f"masukkan harga {makanan} :"))
#     harga = [harga_menu]
#     list_harga.append
    

#     print("\n\n"+ "="*10 + "menu makanan" + "="*10)
#     for i, menu in enumerate(list_menu) :
#         print(f"{i+1} | {menu[0]} | Rp {harga[i]}")

#     print("\n\n" + "="*32)
#     jawaban = input("apakah dilanjutkan?(y/n)").lower()

#     if jawaban == "n" :
#         break

# print("program selesai")

# # program 1
# menu_makanan = []  
# indeks = 0
# while True:
#     print("Masukkan menu")
#     nama_makanan = input("Masukkan nama makanan :")
#     harga = float(input(f"Masukkan Harga :"))
    
#     menu = (nama_makanan, harga)
#     menu_makanan.append(menu)
    

#     print("\n\n" + "=" * 10 + "Menu Makanan" + "=" * 10)
#     for i in range(len(menu_makanan)) :
#         menu = menu_makanan[i]
#         print(f"{i+1} | {menu[0]} | Rp {menu[1]}")

#     print("\n" + "=" * 32)
#     jawaban = input("Apakah dilanjutkan? (y/n)").lower()

#     if jawaban == "n":
#         break
# print("program selesai")

# program 2
data_menu = []

while True :
    jumlah_menu = int(input("Masukkan Jumlah Menu :"))

    if jumlah_menu == 0 :
        break 

    for i in range(jumlah_menu):
        print(f"{i + 1}. Masukkan Data Menu :")
        makanan = input("Makanan: ")
        harga = int(input("Harga: "))
        print()

        menu = (makanan, harga)
        data_menu.append(menu)

    print("\nData Menu:")
    for menu in data_menu:
        print(f"Makanan : {menu[0]}          | Harga : {menu[1]}")

print("Program Selesai")




