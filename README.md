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
•	inisialisasi variabel terdapat pada syntax
``` pyhton
baris = 10
kolom = baris
```

•	Untuk perulangan baris dan kolom menggunakan `nested for`
``` pyhton
for bar in range(baris):
    for col in range(kolom):
        tab=bar+col
```

•	Untuk menampilkan hasil dari perulangan
``` pyhton
 print("{0:>5}".format(tab), end='')
    print()
```
Fungsi `format string` agar text terlihat rapih menggunakan rata ke kanan sebanyak 5 karakter <br>
Fungsi `end=''` agar output tidak membuat baris baru <br>



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
•	Fungsi import random untuk membuat bilangan acak
•	Untuk menentukan jumlah input yang diinginkan dan dikonversi ke dalam bilangan bulat (integer) yang dimasukan ke variable `hasil`
``` pyhton
 hasil = int(input("masukan nilai n: "))
```
•	Untuk pengulangan range yang diinputkan oleh variable `hasil`
``` pyhton
 for i in range(hasil):
```
•	Untuk menampilkan urutan data sesuai jumlah inputan dengan hasil di bawah 0.5
``` pyhton
 angkaDec = random.uniform(0, 0.5)
 print("data ke", i, "=", angkaDec)
```


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
•	Ketiga bilangan akan diinput oleh user dengan syntax seperti dibawah ini
``` pyhton
a=int(input("masukan bilangan pertama: "))
b=int(input("masukan bilangan kedua: "))
c=int(input("masukan ketiga: "))
```
•	Fungsi `if elif else` dibawah ini digunakan sebagai kondisi selection
```python
if a > b > c:
    print(a, "adalah nilai terbesar")
elif b > a and b > c:
    print(b, "adalah nilai terbesar")
else:
    print(c, "adalah nilai terbesar")
 ```
Statement `If` yaitu bila suatu kondisi tertentu tercapai maka apa yang harus dilakukan. <br>
Statement `elif` apabila ketika kondisi lainnya tidak tercapai maka jalankan program. <br>
Sedangkan statement `else` akan berjalan ketika tidak ada suatu kondisi yang terpenuhi pada if dan elif. <br>



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
        e = a*0.2
        print("laba bulan ke ",x,":",e)
total=b+b+c+c+d+d+d+e
print("\Total : ", total)
 ```
#### OUTPUT
Dibawah ini merupakan hasil output dari syntax diatas

![outputprogram1](ss%20gambar/outputprogram1.PNG)

#### ANALISIS
•	Untuk pengulangan range yang diinputkan dengan value 1,9
```python
for x in range(1,9):
 ```
•	Fungsi `if` dibawah ini digunakan sebagai kondisi selection
```python
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
        e = a*0.2
        print("laba bulan ke ",x,":",e)
 ```
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
•	Statement while berfungsi untuk melakukan perulangan
```python
while True:
a=int(input("masukan bilangan : "))
```
While tersebut akan terus memproses variabel `a` yang mencetak `masukan bilangan`
Atau sederhananya user akan diminta terus meninputkan masukan bilangan
•	Sampai apabila user menginputkan angka 0 program akan berhenti
```python
if a == 0:
        break
```
Karena if a == 0 maka break. 
•	Kemudian program akan mencetak nilai terbesar melalui statement

```python
print(max, "merupakan bilangan terbesar")
 ```
 yang diproses dari statement
 ```python
if max < a:
        max = a
 ```


# SEKIAN DAN TERIMAKASIH:)


