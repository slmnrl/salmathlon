### Nama    : Salma Nurul Aziz

### NPM     : 2206028661

### Kelas   : PBP C

Welcome to salmathlon page

Link: https://salmathlon.adaptable.app/main/



### Implementasi Proyek
1. Untuk membuat proyek Django, diperlukan dependencies, yaitu modul yang diperlukan oleh perangkat lunak untuk berfungsi, yang isinya berupa library, framework, atau package. Penggunaan Dependencies ini memerlukan manajemen yang hati-hati, oleh karena itu diperlukan virtual environment untuk mengisolasi dependencies proyek yang berbeda.

Dependencies dapat disiapkan dalam file requirements.txt berikut

<img width="424" alt="Screenshot 2023-09-10 213132" src="https://github.com/slmnrl/salmathlon/assets/124946381/ffc74cf7-1344-4237-b110-bc644697d796">

Kemudian, pasang dependencies yang telah disiapkan dengan perintah
```
pip install -r requirements.txt
```

2. Buat proyek Django bernama `salmathlon` dengan perintah 
```
django-admin startproject salmathlon .
```
Setelah membuat proyek, tambahkan host yang diizinkan untuk mengakses aplikasi web agar aplikasi dapat diakses secara luas

3. Buat aplikasi main pada proyek `salmathlon` dengan perintah
 ```
python manage.py startapp main
 ``` 
Setelah aplikasi main dibuat, tambahkan `main` ke daftar aplikasi yang ada dalam direktori proyek salmathlon agar aplikasi dapat dijalankan.

4. Karena dalam proyek ini kita menggunakan konsep MVT, perlu dibuat template  yang nantinya akan dihubungkan ke views. Berkas yang akan menjadi template adalah `main.html` sebagai berikut

<img width="334" alt="Screenshot 2023-09-12 113551" src="https://github.com/slmnrl/salmathlon/assets/124946381/115460a2-8fa6-4d45-a184-b742f6a8bf89">

5. Membuat model sebagai berikut
<img width="373" alt="Screenshot 2023-09-12 120759" src="https://github.com/slmnrl/salmathlon/assets/124946381/50ff6840-f49e-4a07-a7f0-87e596278511">

Nama model yang didefinisikan adalah Product dengan atribut `name`, `amount`, dan `description`.
Model yang telah didefinisikan ini harus dilakukan migrasi untuk mengubah struktur tabel basis data yang sesuai dengan perintah

```
python manage.py makemigrations
python manage.py migrate
```
6. Membuat fungsi `show_main` yang digunakan untuk mengambil data dari model dan dikembalikan ke template html
<img width="362" alt="Screenshot 2023-09-12 121412" src="https://github.com/slmnrl/salmathlon/assets/124946381/f2917dc8-2e91-453c-b368-5bacc3a2805f">

7. Membuat sebuah routing untuk konfigurasi URL aplikasi `main`
<img width="317" alt="Screenshot 2023-09-12 121742" src="https://github.com/slmnrl/salmathlon/assets/124946381/b16dcbe7-4c73-4871-88ee-f6c55a954d24">

8. Konfigurasi routing url proyek
<img width="324" alt="Screenshot 2023-09-12 121935" src="https://github.com/slmnrl/salmathlon/assets/124946381/246a1087-bfe8-49ee-a86f-d82f02b8e788">

9. Unggah proyek ke repositori GitHub dengan nama salmathlon dan membuat berkas `.gitignore` untuk konfigurasi yang digunakan dalam repositori Git
10. Membuat aplikasi di Adaptable bernama salmathlon dan menyambungkannya dengan GitHub

### Bagan Request Client dan Respon
![bagan](https://github.com/slmnrl/salmathlon/assets/124946381/e3b206a9-bd8a-4920-9bd1-7f8e9f5680ab)
1. Client membuat HTTP request ke URL tertentu di aplikasi Django
2. Aplikasi Django menerima Request
3. Aplikasi Django akan mencocokkan URL yang diterima dengan pola yang didefinisikan dalam berkas urls.py
4. Setelah cocok dengan pola yang didefinisikan di urls.py, Django akan mengarahkan request ke fungsi view yang sesuai
5. Fungsi view (dalam views.py) yang sesuai akan dijalankan untuk menangani request. View dapat berinteraksi dengan model yang didefinisikan dalam models.py. Fungsi ini berisi logika bisnis, pengolahan data, dan persiapan respon. 
6. Setelah selesai memproses request, view akan mengembalikan respon ke template HTM untuk menghasilkan respon HTML yang akan dikirim kembali ke client
7. Template HTML menggabungkan data yang diterima view dengan HTML dan menghasilkan halaman web yang akan ditampilkan kepada client
8. Aplikasi Django mengirimkan respon HTML yang dihasilkan bersama dengan header HTTP ke client
9. Client menerima respon dan menampikan halaman web kepada pengguna

### Penggunaan Virtual Environment
Virtual environment digunakan untuk mengisolasi package serta dependencies dari proyek yang berbeda yang ada di komputer sehingga tidak bertabrakan dengan versi lain yang ada. Kita dapat tetap membuat aplikasi web berbasis Django tanpa menggunakan _virtual environment_ jika hanya dilakukan di dalam lingkungan local server. Pengguna dapat hanya dengan menggunakan environment Python bawaan dari komputer (root) untuk menginstal dependensi yang dibutuhkan proyek Django sehingga proyek Django dapat berjalan di server "local". Namun, jika untuk dijalankan di online hoster hal ini cukup susah dilakukan karena server host akan mencari daftar dependensi yang ada di dalam "requirements.txt" untuk disesuaikan dengan paket dependensi yang dimiliki mesin hosting. Jika "requirements.txt" tidak ada karena tidak diinisialisasikan virtual environmentnya, maka mesin host tidak pernah tahu dependensi apa saja yang diperlukan untuk menjalankan server sehingga proyek juga tidak akan berjalan.

### MVC, MVT, MVVM

**MVT**

Konsep MVT adalah sebuah konsep arsitektur yang digunakan dalam pengembangan web untuk  memisahkan komponen utama sebuah aplikasi menjadi tiga bagian, yaitu Model-View-Template

Model: Menyimpan data dan logika aplikasi.

View: Menampilkan data dari model dan menghubungkannya dengan template.

Template: Menentukan tampilan antarmuka pengguna.

**MVC**

Konsep MVC adalah sebuah konsep arsitektur yang digunakan dalam pengembangan web untuk  memisahkan komponen utama sebuah aplikasi menjadi tiga bagian, yaitu Model-View-Controller.

Model: Menyiapkkan, mengatur, memanipulasi dan mengorganisasikan data yang ada di basis data

View: Menentukan tampilan antarmuka pengguna.

Controller: Menghubungkan serta mengatur model dan view agar dapat saling terhubung

**MVVM**

Konsep MVVM adalah konsep arsitektur yang digunakan untuk pengembangan aplikasi yang berfokus pada pemisahan antara kode untuk logina bisnis dan tampilan aplikasi. MVVM terdiri dari beberapa layer, yaitu Model-View-ViewModel.

Model: Merepresentasikan data yang akan digunakan pada logika bisnis.

View: Berisi antarmuka pengguna dari aplikasi untuk mengatur bagaimana informasi akan ditampilkan.

ViewModel: Bertugas untuk berinteraksi dengan model di mana data yang ada akan diteruskan ke layer view.






