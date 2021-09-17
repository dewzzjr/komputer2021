# TUGAS: BUAT BENTUK DIAMOND 
# DENGAN MENGGUNAKAN 
# PERULANGAN DAN FUNGSI
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *
def diamond(n):
    i = 0
    while i < n:
        print("*", end='')
        i = i + 1

# CONTOH MEMBUAT SEGITIGA
def triangle(n):
    i = 0
    while i < n:
        j = 0
        while j < i:
            print("*", end='')
            j = j + 1
        print('')
        i = i + 1

triangle(10)

diamond(5)