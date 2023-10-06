# inputkan apa yang mereka pilih
# print("permainan gunting, batu, kertas")
# pemain_ke_1 = input("masukkan pilihan pemain ke 1 (gunting/batu/kertas): ")
# pemain_ke_2 = input("masukkan pilihan pemain ke 2 (gunting/kertas/batu): ")


# # jika pemain sudah memilih salah satu maka kita akan membandingkan siapa yang menang
# if pemain_ke_1 == pemain_ke_2:
#     print("Hasil:Sama")
# elif pemain_ke_1 == "gunting":
#     if pemain_ke_2 == "batu":
#         print("pemain 2 menang")
#     else:
#         print("pemain 1 menang")
# elif pemain_ke_1 == "batu":
#     if pemain_ke_2 == "gunting":
#         print("pemain 1 menang")
#     else:
#         print("pemain 2 menang")
# elif pemain_ke_1 == "kertas":
#     if pemain_ke_2 == "batu":
#         print("pemain 1 menang")
#     else:
#         print("pemain 2 menang")
# elif pemain_ke_1 == "batu":
#     if pemain_ke_2 == "kertas":
#         print("pemain 2 menang")
#     else:
#         print("pemain 1 menang")
# elif pemain_ke_1 == "gunting":
#     if pemain_ke_2 == "kertas":
#         print("pemain 1 menang")
#     else:
#         print("pemain 2 menang")
# elif pemain_ke_1 == "kertas":
#     if pemain_ke_2 == "gunting":
#         print("pemain 2 menang")
#     else:
#         print("pemain 1 menang")
# else: 
#     print ("hasil tidak valid, silahkan ulang lagi")

# # Daftar pilihan yang tersedia
# pilihan = ["batu", "gunting", "kertas"]

# # Menampilkan pilihan kepada pengguna
# print("Pilih salah satu dari pilihan berikut:")
# for index, item in enumerate(pilihan, start=1):
#     print(f"{index}. {item}")

# # Meminta input dari pengguna
# while True:
#     try:
#         nomor_pilihan = int(input("Masukkan nomor pilihan Anda: "))
#         if nomor_pilihan < 1 or nomor_pilihan > len(pilihan):
#             print("Pilihan tidak valid. Harap masukkan nomor pilihan yang benar.")
#         else:
#             break
#     except ValueError:
#         print("Masukkan nomor pilihan yang valid.")

# # Mengambil pilihan pengguna berdasarkan nomor yang dimasukkan
# pilihan_pengguna = pilihan[nomor_pilihan - 1]

# # Menampilkan pilihan pengguna
# print(f"Anda memilih: {pilihan_pengguna}")


print ("permainan gunting, batu, kertas")
pemain1 = input("silahkan pilih :").lower()
pemain2 = input("silahkan pilih :").lower()

if pemain1 == pemain2 :
     print (f"{pemain1} vs {pemain2} = seri")
elif pemain1 == "batu" and pemain2== "kertas":
    print (f"{pemain1} vs {pemain2} = {pemain2} menang")
elif pemain1 == "batu" and pemain2== "gunting":
    print (f"{pemain1} vs {pemain2} = {pemain1} menang")
elif pemain1 == "kertas" and pemain2== "gunting":
    print (f"{pemain1} vs {pemain2} = {pemain2} menang")
elif pemain1 == "gunting" and pemain2== "kertas":
    print (f"{pemain1} vs {pemain2} = {pemain1} menang")
elif pemain1 == "kertas" and pemain2== "gunting":
    print (f"{pemain1} vs {pemain2} = {pemain1} menang")
elif pemain1 == "kertas" and pemain2== "batu":
    print (f"{pemain1} vs {pemain2} = {pemain1} menang")
else :
    print ("hasil tidak valid")




    

