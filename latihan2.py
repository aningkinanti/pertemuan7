#author aning kinanti

import random
print(39*"=")
print("author aning kinanti")
print("soal : bilangan acak yang lebih kecil dari 0,5")
print(39*"=")
hasil = int(input("masukan nilai n: "))
i = 0
for i in range(hasil):
    i += 1
    angkaDec = random.uniform(0, 0.5)
    print("data ke", i, "=", angkaDec)