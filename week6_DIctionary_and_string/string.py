import sys

# ==================================== STRING =============================================
# Python akan memulai perhitungan dari nol 
pulau = "kalimantan"
print("\nPulau [2]")
print(pulau[2])
# Saat menggunakan -(minus) maka proses perhitungan akan dimulai dari -1
print("pulau [-2]: ")
print(pulau[-2])
print("//////////")
print("\nPrint liman [2:7]")
print(pulau[2:7])
print("Print limantan [2:]")
print(pulau[2:])
print("Print kali [:4]")
print(pulau[:4])
print("Print kalimantan [:]")
print(pulau[:])

print("\n")
for i in pulau :
    print (i)
print("\n")
for k in range(len(pulau)) :
    print (k)


# SINGKATAN
print("// Program Singkatan //")

kalimat = input("Masukan Kalimat: ")
singkatan = ""
daftar_kata  = kalimat.strip().split(" ")
for kata in daftar_kata :
    singkatan += kata[0].upper()
print(f"Singkatan: {singkatan}")

# # Program pengecekan tanda kurung
# print("====== Selamat datang di program pengecekan tanda kurung =====")
# kata = input("Tolong masukan kalimat beserta tanda kurung: ")
# stack = []
# for i in kata :
#     if i in '([{' : 
#         stack.append(i)
#     elif i in "}])" :
#         if stack :
#             if i == '}' and '{' != stack.pop() :
#                 SystemExit("Tanda {} Salah !!")
#             if i == ']' and '['  != stack.pop() :
#                 SystemExit("Tanda [] Salah !!")
#             if i == ')' and '('  != stack.pop() :
#                 SystemExit("Tanda () Salah !!")
#         else :
#             print("Tidak ada tanda kurung di awal")
# print("Kalimat sudah benar")


# Program pengecekan tanda kurung (improved)
print("\n\n===== Selamat datang di program penngecekan tanda kurung =====\n")
print("Tolong Masukan kalimat dan sertakan salah satu atau semua tanda berikut () {} []\n")
masukan_kalimat = input(": ")
stack = []
for i in masukan_kalimat : 
    if i in '({[' :
        stack.append(i)
    elif i in ']})' :
        if not stack:
            print(f"Error: Ditemukan '{i}' tapi tidak ada kurung buka pasangannya.")
            sys.exit()

        pengecekan = stack.pop()
        if i == ']' and '[' != pengecekan :
            sys.exit(f"Kesalahan ditemukan pada {i} Tanda [] tidak cocok")
        elif i == '}' and '{' != pengecekan :
            sys.exit(f"Kesalahan ditemukan pada {i} Tanda {{}} tidak cocok")
        elif i == ')' and '(' != pengecekan :
            sys.exit(f"Kesalahan ditemukan pada {i} Tanda () tidak cocok")

if stack:
    print(f"Error: Kalimat tidak seimbang. Tanda '{stack[-1]}' tidak ditutup.")
else:
    print("Kalimat sudah benar. Semua tanda kurung seimbang.")