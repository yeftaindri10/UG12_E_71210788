masukkan = int(input("Masukkan angka : "))
def pola(n):
    operasi = 2*n-2
    for i in range(0,n):
        for j in range(0,operasi):
            print(end=" ")
        operasi = operasi - 1
        for j in range(0,i+1):
            print("* ", end="")
        print("\r")
    operasi = n-2
    for i in range(n,-1,-1):
        for j in range(operasi,0,-1):
            print(end=" ")
        operasi = operasi + 1
        for j in range(0,i+1):
            print("* ", end="")
        print("\r")

pola(masukkan)
