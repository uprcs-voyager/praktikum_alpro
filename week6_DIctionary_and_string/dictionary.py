# ===== KODE MODUL PRAKTIKUM MINGGU 6 =======
import pprint
dictionary_buah = {
        "Pisang" : 10000,
        "Apel" : 5000,
        "Mangga" : 4000,
        "Jambu" : 12000
}
# Mengeprint semua dictionary
print("\nIni adalah contoh dictionary, berikut adalah dictionary yang sudah kita buat")
print(dictionary_buah)

# Mengerprint key nya saja
print("\nIni jika kita hanya ingin menge-print key dictionary nya:")
print(dictionary_buah.keys())
# menggunakan pprint

print("\nIni jika kita menggunakan library pprint: ")
pprint.pprint(dictionary_buah)

b = {1: 'Januari', 2: 'Februari', 'Januari' : 1, 'Februari' : 2} 
print(b[2]) 
print(b['Januari']) 
print(b) 


# ===== TOKO BUAH ======
stock = {
        "pisang" : 10,
        "apel" : 5,
        "semangka" : 10,
        "pir" : 3
    }
harga = {
        "pisang" : 1000,
        "apel" : 2000,
        "semangka": 3000,
        "pir" : 4000
    }
choice = 'y'

while (choice == 'y') or (choice == 'Y') : 
    print("\n===== Selamat datang di toko buah =====\n")
    print("Berikut adalah daftar buah yang tersedia:")
    for item, amounts in stock.items() :
        print("{} = {}".format(item, amounts))


    buah = input("\nBuah apa yang ingin anda beli? :")
    jumlah = int(input("\nBerapa jumlah buah yang ingin anda beli? :"))
    if stock[buah] >= jumlah :
        stock[buah] -= jumlah
        total_harga = harga[buah]*jumlah
        print("\n\n== Receipt ==")
        print(f"// anda membeli buah {buah}")
        print(f"// Jumlah pembelian: {jumlah}")
        print(f"Total harga pembelian anda adalah: {total_harga}")
        print("=====================================================\n")
        print(f"Sisa stock {buah} Sekarang adalah: {stock[buah]}")
        choice = input(("\nApakah anda ingin membeli buah lagi? y/n: "))
    else :
        print(f"\n Maaf stock sedang tidak tersedia")
print("baiklah selamat tinggal")


# ===== EXTRA =====
def print_game_item_list(data) :
    print("Daftar Items: ")
    for item, amount in data.items() :
        print("{} ({})".format(item, amount))



inventory = {
        "Sekop" : 4,
        "Medical Kit" : 3,
        "Granat" : 2
    }

print_game_item_list(inventory)