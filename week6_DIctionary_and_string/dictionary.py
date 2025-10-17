# ===== KODE MODUL PRAKTIKUM =======
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





# # ===== EXTRA =====
# def print_game_item_list(data) :
#     print("Daftar Items: ")
#     for item, amount in data.items() :
#         print("{} ({})").format(item, amount)



# inventory = {
#         "Sekop" : 4,
#         "Medical Kit" : 3,
#         "Granat" : 2
#     }