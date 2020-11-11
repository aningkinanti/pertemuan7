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

Penjelasan

1. Mengimport module `random` untuk membuat bilangan acak
```python
import random
```

2. Untuk menentukan jumlah input yang diinginkan dan dikonversi ke dalam bilangan bulat (integer) yang dimasukan ke variable `jum`
```python
jum = int( input("Masukan nilai n : "))
```

3. Untuk pengulangan range yang diinputkan oleh variable `jum`
```python
for i in range(jum):
```

4. Untuk menampilkan urutan data sesuai jumlah inputan dengan hasil di bawah 0.5
```python
angkaDec = random.uniform(0, 0.5)
    print("Data ke", i, " = ", angkaDec)
```

Maka program yang dihasilkan akan seperti berikut

![tampil 2](isi%20foto/hasil%202.png)


### program 1

soal hasil praktikum.....

![GitHub Logo](isi%20foto/tugas%203.png) <h2>

  *Membuat program sederhana dengan perulangan :

 Seorang pengusaha menginvestasikan uangnya untuk memulai usahanya 
dengan modal awal 100 juta,

- Pada bulan pertama dan kedua belum mendapatkan laba.

- Pada bulan ketiga baru mulia mendapatkan laba sebesar 1%

- Pada bulan ke lima pendapatan meningkat 5%

- Pada bulan ke delapan mengalami penurunan keuntungan sebesar 2%, 
sehingga laba menjadi 3%.

- Hitung total keuntungan selama 8 bulan berjalan usahanya.

 *ALGORITMA menghitung keuntungan selama 8 bulan berjalannya usaha.

1. Mulai

2. Mencetak latihan1

3. Mencetak "Program menghitung laba dengan modal awal 100 juta"

4. Membuat Note

5. Mencetak Bulan pertama dan kedua = 0%

6. Mencetak bulan ke 3 = 1%

7. Mencetak bulan ke 5 = 5%

8. Mencetak bulan ke 8 = 2%

9. integer a = 100.000.000( modal awal)

10. Menggunakan fungsi looping for pada nilai x 1-9 untuk menampilkan 
bulan 1 sampai bulan 8.

11. Menggunakan fungsi if, untuk menghitung laba bulan 1 sampai 8

12. bulan pertama dan kedua laba adalah 0

13. bulan ke 3 dan ke 4 mendapat laba 1% sehingga modal di kali 1% = 
keuntungan

14. bulan ke 5 mendapatkan laba 5%, sehingga modal dikali 5% = 
keuntungan

15. Bulan ke 8 mmendapatkan laba 2% sehingga keuntungan menurun dari 
bulan sebelumnya, modal dikali 2% = keuntungan.

16. Menghitung jumlah total laba dengan menjumlah keuntungan dari bulan 
ke 1 sampai bulan 8, hasilnya adalah total keuntungan yang didapat.

17. Selesai

Maka program yang saya buat sebagai berikut atau bisa dilihat di [hasil Code](program1.py)

## Syntax program 1 sebagai berikut :
```python 
#herli

print("------TUGAS PRAKTIKUM 3------")
print("Program Mengitung Laba Dengan Modal 100.000.000")
print("")
print("Note")
print("Bulan Pertama dan ke 2 = 0%")
print("Pada Bulan ke 3 = 1%")
print("Pada Bulan Ke 5 = 5%")
print("Pada Bulan ke 8 = 2%")
print("")

#variable
a = 1000000000
for x in range(1,9):
    if(x>=1 and x<=2):
        b = a*0
        print("Laba bulan ke-",x," : ",b)
    if(x>=3 and x<=4):
        c = a*0.1
        print("Laba bulan ke-",x," : ",c)
    if(x>5 and x<=7):
        d = a*0.5
        print("Laba bulan ke-",x," : ",d)
    if(x==8):
        e = a*0.5
        print("Laba bulan ke-",x," : ",e)
#hasil dari total tersebut
total=b+b+c+c+d+d+e
print("\n Total : ",total)
```

## Hasil output program3 ketika run time adalah sebagai berikut :

# ![GitHub Logo](isi%20foto/hasil%203.png) <h2>
