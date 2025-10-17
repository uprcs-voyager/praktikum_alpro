matriks_A = [
    [3, 8, 5],
    [4, 1, 7]
]

matriks_B = [
    [1, 0, 2],
    [6, 5, 9]
]

if len(matriks_A) != len(matriks_B) or len(matriks_A[0]) != len(matriks_B[0]):
    print("Error: Dimensi matriks tidak sama, tidak bisa dijumlahkan!")
else:
    hasil = [[0, 0, 0], [0, 0, 0]]


    for i in range(len(matriks_A)):
        for j in range(len(matriks_A[0])):
            hasil[i][j] = matriks_A[i][j] + matriks_B[i][j]

    # Cetak hasil
    print("Matriks A:")
    for baris in matriks_A:
        print(baris)

    print("\nMatriks B:")
    for baris in matriks_B:
        print(baris)

    print("\nHasil Penjumlahan:")
    for baris in hasil:
        print(baris)




# list 3 dimensi
# Membuat list 3D
# Dimensi: 2 gudang, 2 rak, 3 barang per rak
data_inventaris = [
    # Gudang 1
    [
        # Rak 1 di Gudang 1
        ["Buku", "Pensil", "Penghapus"],
        # Rak 2 di Gudang 1
        ["Penggaris", "Spidol", "Kertas"]
    ],
    # Gudang 2
    [
        # Rak 1 di Gudang 2
        ["Laptop", "Mouse", "Keyboard"],
        # Rak 2 di Gudang 2
        ["Monitor", "Printer", "Kabel HDMI"]
    ]
]

# --- Mengakses Elemen ---
print("--- Mengakses Elemen Tertentu ---")

# Mengakses barang ke-3 ("Penghapus") di rak ke-1, di gudang ke-1
barang = data_inventaris[0][0][2]
print(f"Barang di Gudang 1, Rak 1, Posisi 3 adalah: {barang}")

# Mengakses barang ke-1 ("Monitor") di rak ke-2, di gudang ke-2
barang_2 = data_inventaris[1][1][0]
print(f"Barang di Gudang 2, Rak 2, Posisi 1 adalah: {barang_2}\n")


# --- Cara Melakukan Iterasi/Looping pada List 3D ---
print("--- Menampilkan Semua Isi Inventaris ---")
# Loop pertama untuk mengakses setiap gudang
for i in range(len(data_inventaris)):
    print(f"Isi Gudang ke-{i+1}:")
    # Loop kedua untuk mengakses setiap rak di dalam gudang
    for j in range(len(data_inventaris[i])):
        print(f"  Rak ke-{j+1}: {data_inventaris[i][j]}")
    print("-" * 20) # Pemisah antar gudang