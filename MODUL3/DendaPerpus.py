# program denda peminjaman buku perpustakaan

while True:
    lama_peminjaman = int(input("Masukkan lama peminjaman buku (dalam hari): "))

    denda = 0
    if lama_peminjaman > 7:
        denda = (lama_peminjaman - 7) * 2000
        minggu_lewat = (lama_peminjaman - 7) //7
        denda += minggu_lewat * 5000

    print("Denda yang harus dibayar: Rp", denda)

    jawaban = input("Apakah Anda ingin menghitung lagi? (ya/tidak): ")
    if jawaban.lower() != "ya":
        break 

