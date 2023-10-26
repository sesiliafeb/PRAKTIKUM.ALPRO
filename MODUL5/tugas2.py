# print("Masukkan menu")
#     makanan = input("Masukkan nama makanan: ")
#     menu = [makanan]
#     list_menu.append(menu)

#     harga_menu = float(input(f"Masukkan harga {makanan}: "))
#     harga = [harga_menu]
#     list_harga.append(harga)

#     print("\n\n" + "=" * 10 + "Menu Makanan" + "=" * 10)
#     for i, menu in enumerate(list_menu):
#         print(f"{i+1} | {menu[0]} | Rp {list_harga[i]}")

#     print("\n" + "=" * 32)
#     jawaban = input("Apakah dilanjutkan? (y/n)").lower()

#     if jawaban == "n":
#         break
# print("program selesai")

# # Fungsi untuk mencari mahasiswa berdasarkan Prodi
# def cari_mahasiswa_berdasarkan_prodi(data_mahasiswa, prodi):
#     mahasiswa_ditemukan = []
#     for mahasiswa in data_mahasiswa:
#         if mahasiswa[2] == prodi:
#             mahasiswa_ditemukan.append(mahasiswa)
#     return mahasiswa_ditemukan

# # Input data mahasiswa
# data_mahasiswa = []

# jumlah_mahasiswa = int(input("Masukkan Jumlah Data :"))  # Ubah sesuai dengan jumlah mahasiswa yang ingin dimasukkan

# for i in range(jumlah_mahasiswa):
#     print(f"{i + 1}. Masukkan data mahasiswa")
#     nama = input("Nama: ")
#     nim = int(input("NIM: "))
#     prodi = input("Program Studi: ")
#     alamat = input("Alamat: ")
#     print()

#     mahasiswa = (nama, nim, prodi, alamat)
#     data_mahasiswa.append(mahasiswa)


# # Tampilan data mahasiswa
# print("\nData Mahasiswa:")
# for mahasiswa in data_mahasiswa:
#      print(f"NIM : {mahasiswa[0]} | Nama : {mahasiswa[1]} | Prodi : {mahasiswa[2]} | Alamat : {mahasiswa[3]}")


# # Cari mahasiswa berdasarkan Prodi
# cari_prodi = input("\nMasukkan Program Studi yang ingin dicari: ")
# mahasiswa_ditemukan = cari_mahasiswa_berdasarkan_prodi(data_mahasiswa, cari_prodi)

# # Tampilan data cari prodi
# print("\nData Mahasiswa Yang di Cari:")
# for mahasiswa in mahasiswa_ditemukan:
#      print(f"NIM : {mahasiswa[0]} | Nama : {mahasiswa[1]} | Prodi : {mahasiswa[2]} | Alamat : {mahasiswa[3]}")


def cari_mahasiswa_berdasarkan_prodi(data_mahasiswa, prodi):
    mahasiswa_ditemukan = []
    for mahasiswa in data_mahasiswa:
        if mahasiswa[2] == prodi:
            mahasiswa_ditemukan.append(mahasiswa)
    return mahasiswa_ditemukan

data_mahasiswa = []
while True :
    jumlah_mahasiswa = int(input("Masukkan Jumlah Data :"))

    if jumlah_mahasiswa == 0 :
        break 

    for i in range(jumlah_mahasiswa):
        print(f"{i + 1}. Masukkan data mahasiswa")
        nama = input("Nama: ")
        nim = int(input("NIM: "))
        prodi = input("Program Studi: ")
        alamat = input("Alamat: ")
        print()

        mahasiswa = (nama, nim, prodi, alamat)
        data_mahasiswa.append(mahasiswa)

    print("\nData Mahasiswa:")
    for mahasiswa in data_mahasiswa:
        print(f"NIM : {mahasiswa[0]} | Nama : {mahasiswa[1]} | Prodi : {mahasiswa[2]} | Alamat : {mahasiswa[3]}")

    cari_prodi = input("\nMasukkan Program Studi yang ingin dicari: ")
    mahasiswa_ditemukan = cari_mahasiswa_berdasarkan_prodi(data_mahasiswa, cari_prodi)

    print("\nData Mahasiswa Yang di Cari:")
    for mahasiswa in mahasiswa_ditemukan:
        print(f"NIM : {mahasiswa[0]} | Nama : {mahasiswa[1]} | Prodi : {mahasiswa[2]} | Alamat : {mahasiswa[3]}")
print("Program Selesai")

# # cara 2 Fungsi untuk mencari mahasiswa berdasarkan Prodi
# def cari_mahasiswa_berdasarkan_prodi(data_mahasiswa, prodi):
#     mahasiswa_ditemukan = []
#     for mahasiswa in data_mahasiswa:
#         if mahasiswa[3] == prodi:
#             mahasiswa_ditemukan.append(mahasiswa)
#     return mahasiswa_ditemukan

# # Input data mahasiswa
# data_mahasiswa = []

# jumlah_mahasiswa = int(input("Masukkan Jumlah Mahasiswa :"))  # Ubah sesuai dengan jumlah mahasiswa yang ingin dimasukkan

# for i in range(jumlah_mahasiswa):
#     print(f"{i + 1}. Masukkan data mahasiswa")
#     nama = input("Nama: ")
#     nim = int(input("NIM: "))
#     alamat = input("Alamat: ")
#     prodi = input("Program Studi: ")
#     print()
        
#     mahasiswa = (nama, nim, alamat, prodi)
#     data_mahasiswa.append(mahasiswa)


#     # Tampilkan data mahasiswa
    
#     for mahasiswa in data_mahasiswa:
#         print(f"NIM: {mahasiswa[0]} | Nama: {mahasiswa[1]} | Alamat: {mahasiswa[2]} | Prodi: {mahasiswa[3]}")
    
    
    
#     # Cari mahasiswa berdasarkan Prodi
#     cari_prodi = input("\nMasukkan Program Studi yang ingin dicari: ")
#     mahasiswa_ditemukan = cari_mahasiswa_berdasarkan_prodi(data_mahasiswa, cari_prodi)