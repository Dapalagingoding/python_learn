"""
str (string) adalah tipe data untuk teks. Secara teknis ia berupa urutan karakter Unicode yang immutable.
"""

# MATERI 1 MENULIS STRING

a = 'halo'
b = "hallo"
c = """ hallo
semuanya
"""
# yang c itu multi line string

""" 
hirarki string 
1. kutip " didalam kutip '
2. kutip ' didalam kutip "
"""
# nomer 1
d = "dia bilang 'hallo' ke aku"

# nomer 2
e = 'dia bilang "hallo" ke dia'

# MATERI 2 ESCAPE CHARACTER
"""
berikut adalah beberapa code escape character :
1. \n -> berfungsi untuk membuat baris baru
2. \t -> fungsi untuk tab alias triple space
3. \\ ->  mencetak character : \
4. \' -> mencetak character : '
5. \" -> mencetak character : "
6. \r -> replace character
7. \a -> mengeluarkan "beep" pada terminal
8. \b -> backspace

catatan : 
1. ada satu fungsi yang bisa membuat character asli dari escpae character yaitu : repr()
2. "r" (raw string) ini berfungsi untuk mematikan fungsi dari escape character dan mengubahnya jadi teks biasa
"""

# 1. \n
print("hallo \n world")
# menggunakan r
print(r"hello \n world")

# 2. \t
print("hello \t world")

# 3. \\ - \' -\"
print("hello \\ world")
print("hello \' world")
print("hello \" world")

# 4 \r
print("hello \r world")
# ini akan mengganti kata hello menjadi world

# 5 \b
print("hello \b backspace")
# menghapus satu karakter sebelum \b

# MATERI 3 IMMUTABLE, INDEXING, AND SLICING

# INDEXING
s = "PYTHON"
#    012345      (positif)
#   -6-5-4-3-2-1 (negatif)

print(s[0])      # P
print(s[-1])     # N
print(s[1:4])    # YTH   (index 1 sampai 3, ujung tidak ikut)
print(s[:3])     # PYT
print(s[3:])     # HON
print(s[::2])    # PTO   (loncat 2)
print(s[::-1])   # NOHTYP (dibalik)

# IMMUTABLE
"""String tidak bisa diubah setelah dibuat"""
t = "halo"
# t[0]  = "H" ->  ini akan menyebabkan error IMMUTABLE

# cara nya agar bisa di ganti adalah

# 1. menulis secara manual semuanya
t = "Halo"

# 2. manipulasi menggunakan INDEXING
t = "H" + t[1:]
print(t)

# MATERI 4 Operasi dasar
# MATERI 5 METODE
# MATERI 6 Formatting string
# MATERI 7 Konversi
# MATERI 8 Unicode dan encoding
