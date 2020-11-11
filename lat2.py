#author aningkinanti

print("program menampilkan bilangan terbesar dari n buah data yang diinputkan.")
print("lalu masukkan angka 0 untuk berhenti.")

max = 0
while True:
    a=int(input("masukan bilangan : "))
    if max < a:
        max = a
    if a == 0:
        break
print(max, "merupakan bilangan terbesar")