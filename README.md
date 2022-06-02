# Tugas Besar Pemrograman Berorientasi Objek
 
## Nama dan NIM Anggota Kelompok

| Nama                          | NIM       |
| ----------------------------- | --------- |
| Ilham Fadhlur Rahman          | 120140125 |
| Ahmad Advissalam Pakaya       | 120140126 |
| Alga Fiky                     | 120140121 |
| Nadhea Deni Putri             | 120140128 |
| Ichza Auliya Gumilar          | 120140188 |
| Alvian Manshurin              | 120140162 |



## Purpose
Tujuan dari pembuatan game kali ini adalah untuk memenuhi **Tugas Besar Pemrograman Berorientasi Objek ITERA 2022**.

## Space Battle
**Space Battle** adalah sebuah game yang mengharuskan user untuk menjaga pesawat miliknya, supaya dapat bertahan di dalam game dalam waktu yang lama. Sehingga, ketika user mengalahkan Boss yang ada di dalam game, maka user akan memenangkan game. Jika health point yang dimiliki user telah habis, karena sering di serang oleh musuh, maka user akan mengalami kekalahan. Di dalam game juga terdapat jumlah score yang telah di dapatkan oleh user.

## Library
Disini saya menggunakan beberapa library yang telah disediakan oleh Python sendiri, yaitu:

1.  [Pygame](https://www.pygame.org/news). Pygame adalah sebuah kumpulan modul [Python](https://www.python.org/) lintas platform yang dirancang untuk pembuatan video games.
2.  [math](https://docs.python.org/3/library/math.html). math adalah seperangkat fungsi matematika bawaan yang disediakan oleh [Python](https://www.python.org/), termasuk didalamnya modul matematika bawaan, yang memudahkan kita dalam pembuatan game kali ini yang memerlukan koordinat dalam menentukan posisi dari masing-masing kelas.
3.  [sys](https://docs.python.org/3/library/sys.html). sys adalah modul yang disediakan oleh [Python](https://www.python.org/) yang didalamnya terdapat berbagai fungsi dan variabel yang digunakan untuk memanipulasi berbagai bagian Python runtime environment.
4.  [time](https://docs.python.org/3/library/time.html). time adalah modul yang disediakan oleh [Python](https://www.python.org/) yang memiliki berbagai fungsi yang berhubungan dengan waktu.
5.  [random](https://docs.python.org/3/library/random.html). random adalah modul bawaan dari [Python](https://www.python.org/) yang dapat kita gunakan untuk membuat random numbers (angka acak).
6.  [os](https://docs.python.org/3/library/os.html). os adalah modul di [Python](https://www.python.org/) yang menyediakan fungsi untuk berinteraksi dengan Sistem Operasi. 

## Installation
Untuk dapat memainkan game **Space Battle**, user diharapkan untuk melakukan beberapa langkah berikut ini.

1. User diharapkan untuk men-download folder ZIP yang tersedia pada tombol **Code** yang terdapat pada bagian atas github ini. Atau, user juga dapat meng-kloning source code github ini. Cukup mengetik-kan baris kata berikut di dalam command line.
   ```Python
   git clone https://github.com/CaamVilvactDJavu/TugasBesar-PBO
   ```
2. User juga diharuskan untuk meng-install Pygame, karena jika tidak maka game tidak akan bisa berjalan. Instalasinya cukup mudah, dengan cara mengetik-kan beberapa baris kata berikut di dalam command line.
    ```Python
    pip install pygame
   ```

## How to Play
Jika ingin masuk ke dalam game tinggal mengetik-kan.
   ```Python
   python main.py
   ```
Game ini adalah game yang sangat mudah untuk dimainkan. Kita hanya disuruh untuk melawan pesawat musuh dengan menggunakan tembakan, jika musuh kalah maka pesawat musuh akan hancur yang membuat kita mendapatkan score. Musuh juga menggunakan tembakan yang akan membuat health (darah) kita berkurang setiap terkena serangan. Health kita juga akan berkurang, jika musuh mengenai pesawat kita. Di dalam game juga terdapat fitur menambah health (darah) kita, dengan mendekatkan pesawat kita kepada health pack. 

Game ini menggunakan beberapa tombol yang ada pada keyboard, seperti:

- Left-Arrow : untuk membuat pesawat kita bergerak ke kiri.
- Right-Arrow : untuk membuat pesawat kita bergerak ke kanan.
- Up-Arrow : untuk membuat pesawat kita mengeluarkan tembakan.
  
## Game View
- **Tampilan Menu Game**
  ![alt tex](assets/images/TampilanMenu.png)
- **Tampilan Gameplay**
  ![alt tex](assets/images/TampilanGameplay.png)
- **Tampilan Game Berakhir**
  ![alt tex](assets/images/TampilanGameBerakhir.png)

