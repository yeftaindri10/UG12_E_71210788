awal = int(input("Masukkan awal deret : "))
akhir = int(input("Masukkan akhir deret : "))
if (awal + 1) % 2 == 0:
    for i in range(awal + 1, akhir, 2):
        if i % 5 == 0 or i % 9 == 0: continue
        print(i, end=" ")
else:
    for i in range(awal, akhir, 2):
        if i % 5 == 0 or i % 9 == 0: continue
        print(i, end=" ")