def nilai_maksimal(n):
    nilai_terbesar = n[0]
    for nilai in n:
        if nilai>nilai_terbesar:
            nilai_terbesar = nilai
    return nilai_terbesar
def nilai_minimal(n):
    nilai_terkecil = n[0]
    for nilai in n:
        if nilai<nilai_terkecil:
            nilai_terkecil = nilai
    return nilai_terkecil

bilangan=[3, 20, 100, -35, 50]
print(bilangan)
print('Nilai terbesar:', nilai_maksimal(bilangan))
print('Nilai terkecil:', nilai_minimal(bilangan))
print(" ")
bilangan2=[3, 20, 90, 35, 75]
print(bilangan2)
print('Nilai terbesar:', nilai_maksimal(bilangan2))
print('Nilai terkecil:', nilai_minimal(bilangan2))
