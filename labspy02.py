#author aningkinanti

print("program mencari bilangan terbesar dari 3 bilangan menggunakan if")

a=int(input("masukan bilangan pertama: "))
b=int(input("masukan bilangan kedua: "))
c=int(input("masukan ketiga: "))
if a > b > c:
    print(a, "adalah nilai terbesar")
elif b > a and b > c:
    print(b, "adalah nilai terbesar")
else:
    print(c, "adalah nilai terbesar")