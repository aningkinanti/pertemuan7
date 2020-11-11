# TUGAS PERTEMUAN 7 BESERTA PENJELASANNYA
## Kondisi dan Perulangan
***
**Nama	  : Aning Kinanti** <br>
**Nim	    : 312010364** <br>
**Kelas	  : TI.20.A2** <br>
**Matkul	: Bahasa Pemrograman** <br>

## Latihan 1 

![soallatihan1](ss%20gambar/soallatihan1.PNG)

#### SYNTAX
berikut merupakan syntax untuk menampilkan program diatas

```python
#author aningkinanti

baris = 10
kolom = baris

for bar in range(baris):
    for col in range(kolom):
        tab=bar+col
        print("{0:>5}".format(tab), end='')
    print()
```

#### OUTPUT
Dibawah ini merupakan hasil output dari syntax diatas

![outputlatihan1](ss%20gambar/outputlatihan1.PNG)

#### ANALISIS
BELUMMM


## Latihan 2

![soallatihan2](ss%20gambar/soallatihan2.PNG)

#### SYNTAX
berikut merupakan syntax untuk menampilkan program diatas

```python
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
 ```
#### OUTPUT
Dibawah ini merupakan hasil output dari syntax diatas

![outputlatihan2](ss%20gambar/outputlatihan2.PNG)

#### ANALISIS
BELUMMM

## Labspy 2

![soallabspy02](ss%20gambar/soallabspy02.PNG)

#### SYNTAX
berikut merupakan syntax untuk menampilkan program diatas

```python
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
 ```
 
#### OUTPUT
Dibawah ini merupakan hasil output dari syntax diatas

![outputlabspy02](ss%20gambar/outputlabspy02.PNG)

#### ANALISIS
BELUMMM


## Program1

![soalProgram1](ss%20gambar/soalProgram1.PNG)

#### SYNTAX
berikut merupakan syntax untuk menampilkan program diatas

```python
#author aningkinanti

a = 100000000
for x in range(1,9):
    if(x>=1 and x<=2):
        b = a*0
        print("laba bulan ke ",x,":",b)
    if(x>=3 and x<=4):
        c = a*0.1
        print("laba bulan ke ",x,":",c)
    if(x>=5 and x<=7):
        d = a*0.5
        print("laba bulan ke ",x,":",d)
    if(x==8):
        e = a*0.5
        print("laba bulan ke ",x,":",e)
total=b+b+c+c+d+d+d+e
print("\Total : ", total)
 ```
#### OUTPUT
Dibawah ini merupakan hasil output dari syntax diatas

![outputprogram1](ss%20gambar/outputprogram1.PNG)

#### ANALISIS
BELUMMM

## Lat 2

![soalLat2](ss%20gambar/soalLat2.PNG)

#### SYNTAX
berikut merupakan syntax untuk menampilkan program diatas

```python
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
 ```
 
#### OUTPUT
Dibawah ini merupakan hasil output dari syntax diatas

![outputlat2](ss%20gambar/outputlat2.PNG)

#### ANALISIS
BELUMMM

