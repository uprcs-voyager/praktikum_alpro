import time

# definition of a function
'''
fungsi adalah blok kode yang melakukan tugas tertentu dan dapat di panggil berkali-kali. 
dengan memakai fungsi kita tidak perlu menulis kembali kode yang sama.
Oleh karena itu, program akan lebih ter-organisir, mudah dikelola dan lebih efisien

Setiap function biasanya memiliki nama unik dan bisa menerima input dalam bentuk parameter, 
sehingga dapat bekerja dengan data yang berbeda-beda setiap kali dipanggil. 
Function juga bisa mengembalikan nilai sebagai output, memungkinkan hasil dari operasinya dipakai di tempat lain dalam program
''' 

# Making a function
# gunakan def ketika anda ingin membuat suatu fungsi di python
# contoh : def nama_Fungsi()

# Membuat fungsi yang akan mencetak lirik lagu saat di panggil
def cetak_lirik() :
    print("///// I Really Want to Stay at Your House /////")
    print("-- Rosa Walton & Hallie Coggins --\n")
    time.sleep(3)
    print("I couldn't wait for you to come and clear the cupboards")
    print("But now you're gone and leaving nothing but a sign")
    print("Another evening, I'll be sitting reading in-between your lines")
    print("Because I miss you all the time")
    time.sleep(5)
    print("\nSo, get away")
    print("Another way to feel what you didn't want yourself to know")
    print("And let yourself go")

print("\n")
print(cetak_lirik)
print(type(cetak_lirik))
print("\n")
print("\n")

# Memanggil suatu fungsi. Kali ini kita akan memanggik fungsi cetak_lirik()
# cetak_lirik()

# Memanggil fungsi di dalam fungsi yang lain 
def ulangi_lirik() :
    print("\n\n")
    cetak_lirik()
    cetak_lirik()
    cetak_lirik()


# ulangi_lirik()

# Default argumen pada fungsi 
'''kita dapat menetapkan argumen default, jika argumen tersebut tidak tersedia saat pemanggil fungsi'''

def cetak_nama( nama = "lah nggak ada argumennya" ) :
    print(f"\nHalo {nama}\n")

# cetak_nama() # <-- memanggil fungsi cetak_nama tanpa menggunakan argumen
# cetak_nama("ilham asik dari jawa ") # <--memanggil fungsi cetak_nama tanpa menggunakan argumen

