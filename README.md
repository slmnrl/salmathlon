### Nama    : Salma Nurul Aziz

### NPM     : 2206028661

### Kelas   : PBP C

Welcome to salmathlon page

Link: https://salmathlon.adaptable.app/main/

## Implementasi Proyek
1. Untuk membuat proyek Django, diperlukan dependencies, yaitu modul yang diperlukan oleh perangkat lunak untuk berfungsi, yang isinya berupa library, framework, atau package. Penggunaan Dependencies ini memerlukan manajemen yang hati-hati, oleh karena itu diperlukan virtual environment untuk mengisolasi dependencies proyek yang berbeda. Dependencies dapat disiapkan dalam file requirements.txt berikut <img width="424" alt="Screenshot 2023-09-10 213132" src="https://github.com/slmnrl/salmathlon/assets/124946381/00f4c70a-556e-4e73-bdc3-c35acf02d45f">


Kemudian, pasang dependencies yang telah disiapkan dengan perintah
```
pip install -r requirements.txt
```

2. Buat proyek Django bernama `salmathlon` dengan perintah
```
django-admin startproject salmathlon .
```
Setelah membuat proyek, tambahkan host yang diizinkan untuk mengakses aplikasi web agar aplikasi dapat diakses secara luas


3. Buat aplikasi bernama main pada proyek `salmathlon` dengan perintah
 ```
python manage.py startapp main
 ``` 
Setelah aplikasi main dibuat, tambahkan `main` ke daftar aplikasi yang ada dalam direktori proyek salmathlon agar aplikasi dapat dijalankan.

4. Karena dalam proyek ini kita menggunakan konsep MVT, perlu dibuat template  yang nantinya akan dihubungkan ke views. Berkas yang akan menjadi template adalah `main.html` sebagai berikut 

<img width="334" alt="Screenshot 2023-09-12 113551" src="https://github.com/slmnrl/salmathlon/assets/124946381/d5300457-03f0-447a-8223-66e40ed2fc15">

5. Membuat model sebagai berikut
   
<img width="373" alt="Screenshot 2023-09-12 120759" src="https://github.com/slmnrl/salmathlon/assets/124946381/dcffd4cf-a2c1-46af-b3ff-06df809eb42f">

Nama model yang didefinisikan adalah Product dengan atribut `name`, `amount`, dan `description`.
Model yang telah didefinisikan ini harus dilakukan migrasi untuk mengubah struktur tabel basis data yang sesuai dengan perintah

```
python manage.py makemigrations
python manage.py migrate
```
6. Membuat fungsi `show_main` yang digunakan untuk mengambil data dari model dan dikembalikan ke template html 

<img width="362" alt="Screenshot 2023-09-12 121412" src="https://github.com/slmnrl/salmathlon/assets/124946381/6b9a0225-84cb-4399-8915-3afea53f06d0">

7. Membuat sebuah routing untuk konfigurasi URL aplikasi `main`

<img width="317" alt="Screenshot 2023-09-12 121742" src="https://github.com/slmnrl/salmathlon/assets/124946381/caa3750f-9d3a-4495-8642-7f9a3d1530e9">

8. Konfigurasi routing url proyek 

<img width="324" alt="Screenshot 2023-09-12 121935" src="https://github.com/slmnrl/salmathlon/assets/124946381/eec43013-7a1e-4435-b990-de8d8a8cce89">

9. Unggah proyek ke repositori GitHub dengan nama salmathlon dan membuat berkas `.gitignore` untuk konfigurasi yang digunakan dalam repositori Git

10. Membuat aplikasi di Adaptable bernama salmathlon dan menyambungkannya dengan GitHub

## Bagan Request Client dan Respon
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


## Penggunaan Virtual Environment
Virtual environment digunakan untuk mengisolasi package serta dependencies dari proyek yang berbeda yang ada di komputer sehingga tidak bertabrakan dengan versi lain yang ada. Kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan _virtual environment_ jika hanya dilakukan di dalam lingkungan local server. Pengguna dapat hanya dengan menggunakan environment Python bawaan dari komputer (root) untuk menginstal dependensi yang dibutuhkan proyek Django sehingga proyek Django dapat berjalan di server "local". Namun, jika untuk dijalankan di online hoster hal ini cukup susah dilakukan karena server host akan mencari daftar dependensi yang ada di dalam "requirements.txt" untuk disesuaikan dengan paket dependensi yang dimiliki mesin hosting. Jika "requirements.txt" tidak ada karena tidak diinisialisasikan virtual environmentnya, maka mesin host tidak pernah tahu dependensi apa saja yang diperlukan untuk menjalankan server sehingga proyek juga tidak akan berjalan.

## MVC, MVT, MVVM

**MVT**

Konsep MVT adalah sebuah konsep arsitektur yang digunakan dalam pengembangan web untuk  memisahkan komponen utama sebuah aplikasi menjadi tiga bagian, yaitu Model-View-Template.

Model: Menyimpan data dan logika aplikasi.

View: Menampilkan data dari model dan menghubungkannya dengan template.

Template: Menentukan tampilan antarmuka pengguna.

Dalam MVT, View yang menjembatani antara data yang akan diambil dalam Model dan akan ditampilkan di Template.

**MVC**

Konsep MVC adalah sebuah konsep arsitektur yang digunakan dalam pengembangan web untuk  memisahkan komponen utama sebuah aplikasi menjadi tiga bagian, yaitu Model-View-Controller.

Model: Menyiapkkan, mengatur, memanipulasi dan mengorganisasikan data yang ada di basis data.

View: Menentukan tampilan antarmuka pengguna.

Controller: Menghubungkan serta mengatur model dan view agar dapat saling terhubung.

Perbedaan utama dengan MVC adalah bahwa Controller bertindak sebagai perantara antara Model dan View. Ketika pengguna berinteraksi dengan View, Controller mengambil tindakan yang sesuai dan memperbarui Model atau View sesuai kebutuhan.

**MVVM**

Konsep MVVM adalah konsep arsitektur yang digunakan untuk pengembangan aplikasi yang berfokus pada pemisahan antara kode untuk logina bisnis dan tampilan aplikasi. MVVM terdiri dari beberapa layer, yaitu Model-View-ViewModel.

Model: Merepresentasikan data yang akan digunakan pada logika bisnis.

View: Berisi antarmuka pengguna dari aplikasi untuk mengatur bagaimana informasi akan ditampilkan.

ViewModel: Bertugas untuk berinteraksi dengan model di mana data yang ada akan diteruskan ke layer view.

Perbedaan utama dengan MVVM adalah peran ViewModel yang kuat dalam mengatur interaksi antara Model dan View. ViewModel berfungsi sebagai jembatan antara Model dan View, sehingga View tidak perlu memiliki pengetahuan tentang Model.

## PERBEDAAN `POST` DAN `GET`
POST: Digunakan untuk mengirim data ke server untuk disimpan atau diproses lebih lanjut. Jika permintaan `POST` berhasil, server akan merespons dengan kode status HTTP 200(OK).

GET: Digunakan untuk mengambil atau membaca data dari server ketika ingin mendapatkan data dari server tanpa mengubahnya. Jika permintaan `GET` berhasil, server akan merespons dengan kode status HTTP 201(Created).

## PERBEDAAN XML, JSON, DAN HTML DALAM KONTEKS PENGIRIMAN DATA

**XML (eXtensible Markup Language)**
Format      : XML menyimpan data dalam struktur pohon dengan namespace untuk kategori data yang berbeda.
Syntax      : Terdapat beberapa karakter yang digantikan dengan entity references, sehingga lebih bertele-tele.
Parsing     : Menggunakan XML DOM (Document Object Model).
Data types  : XML mendukung data type number, object, string, Boolean arrays, Boolean, date, image, namespaces.

XML biasa digunakan untuk pertukaran data yang sangat terstruktur dan memungkinkan untuk mendefinisikan format data kustom melalui DTD (Document Data Definition) atau XML Schema. Banyak digunakan untuk pertukaran data antara aplikasi yang berbeda.

**JSON (JavaScript Object Nation)**
Format      : Menyimpan data dalam bentuk key-value pairs.
Syntax      : Ringkas dan mudah dibaca serta ditulis.
Parsing     : Dengan fungsi JavaScript JSON.parse()
Data types  : JSON mendukung data type number, object, string, Boolean arrays.

JSON biasa digunakan untuk pertukaran data ringan dan mudah dibaca oleh mesin maupun manusia. Banyak digunakan untuk pengembangan web dan API.

**HTML (HyperText Markup Language)**
Format      : Markup formatting language for the web. Menggambarkan struktur halaman web secara semantik.
Syntax      : Menggunakan tag dan elemen untuk menggambarkan konten web dengan markup yang khusus untuk tampilan halaman.
Parsing     : Tidak diperlukan parsing khusus karena browser web secara otomatis mengurai dan menampilkan halaman web berdasarkan markup HTML.
Data Types: HTML tidak mendukung data types seperti XML atau JSON. Ini adalah bahasa untuk menggambarkan struktur dan tampilan konten web.

HTML biasa digunakan untuk membuat struktur dan tampilan halaman web, termasuk teks, gambar, link, dan elemen-elemen lainnya yang dapat dilihat oleh pengguna melalui browser.

## MENGAPA JSON SERING DIGUNAKAN DALAM PERTUKARAN DATA ANTARA APLIKASI WEB MODERN?
1. Ringan dan Mudah Dibaca: JSON menggunakan format teks yang ringan dan mudah dibaca oleh manusia, sehingga memudahkan pengembang untuk memahami data yang dikirimkan dan diterima.
2. Mendukung Struktur Data Terstruktur: JSON mendukung struktur data yang terstruktur, seperti objek dan array, sehingga memungkinkan representasi data yang kompleks dan bersarang.
3. Kompatibel dengan JavaScript: JSON adalah format data yang berasal dari JavaScript, sehingga mudah diolah dan dipahami oleh bahasa pemrograman JavaScript. Hal ini membuatnya menjadi pilihan yang alami untuk aplikasi web yang berbasis JavaScript.
4. Dukungan untuk Aplikasi API: JSON sering digunakan dalam pembuatan dan konsumsi API (Application Programming Interface) karena kemudahan dalam mengirim dan menerima data melalui HTTP dengan format JSON. Ini membuatnya sangat cocok untuk komunikasi antara aplikasi web dan server.
5. Mendukung Banyak Tipe Data: JSON mendukung tipe data yang umum seperti string, angka, boolean, objek, dan array, sehingga cocok untuk representasi berbagai jenis data.
6. Tidak memiliki batasan lisensi
7. Populer dan banyak digunakan sehingga pemakaian menjadi lebih umum

## IMPLEMENTASI CHECKLIST
1. Form dibuat dengan menambahkan kode berikut
```
from django.forms import ModelForm
from main.models import Item

class ProdutForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "amount", "description"]
```
Ketika form yang berisi `name`, `amount`, dan `description` diisi oleh user, isi dari form akan disimpan menjadi object `Item`.

Pada berkas `views.py`, kita menambahkan `ProductForm` yang telah dibuat. Untuk mengimplementasikan penyimpanan form dan penambahan data produk secara otomats ke tampilan web, buat fungsi baru dengan nama `create_product`.
```
def create_product(request):
    form = ProdutForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)
```
Fungsi ini digunakan untuk membuat ProductForm yang diisi berdasarkan input user dari `request.POST`. Ketika isi input dari form sudah valid, form akan disimpan. 

Untuk menampilkan data yang telah diinput oleh user ke halaman web, kita perlu menambahkan variabel `items` dalam fungsi `show_main` yang akan menyimpan data object Item yang tersimpan pada database. 

Fungsi `create_product` yang telah dibuat juga perlu ditambahkan ke daftar url yang dapat diakses.

Form yang ditampilkan ke pengguna dibuat dengan cara membuat file html baru yang berisi method `POST` untuk mendapat data diinput user. Form tersebut dapat diakses dengan mengeklik  tombol "Add New Product". Data produk yang telah diinput oleh user juga akan ditambahkan ke halaman form dengan kode tambahan berikut
```
...
<table>
    <tr>
        <th>Name</th>
        <th>Price</th>
        <th>Description</th>
        <th>Date Added</th>
    </tr>

    {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini {% endcomment %}

    {% for product in products %}
        <tr>
            <td>{{product.name}}</td>
            <td>{{product.price}}</td>
            <td>{{product.description}}</td>
            <td>{{product.date_added}}</td>
        </tr>
    {% endfor %}
</table>

<br />

<a href="{% url 'main:create_product' %}">
    <button>
        Add New Product
    </button>
</a>
```

## FUNGSI YANG ADA DI `views.py` 
Buat fungsi `show_xml` sebagai berikut
```
def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
Fungsi ini menyimpan hasil query dari seluruh data yang ada pada Item dan mengembalikan objek model menjadi format XML dengan serializers yang terdapat pada HttpResponse.

Buat fungsi `show_json` sebagai berikut
```
def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
Fungsi ini menyimpan hasil query dari seluruh data yang ada pada Item dan mengembalikan objek model menjadi format JSON dengan serializers yang terdapat pada HttpResponse. 

Buat fungsi `show_xml_by_id` sebagai berikut
```
def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
Sama seperti fungsi-fungsi di atas, fungsi ini akan mengembalikan data dalam format XML, namun data yang dikembalikan hanyalah data sesuai id yang diminta. 

```
def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
Sama seperti fungsi-fungsi di atas, fungsi ini akan mengembalikan data dalam format JSON, namun data yang dikembalikan hanyalah data sesuai id yang diminta. 

## MEMBUAT ROUTING URL UNTUK FUNGSI YANG ADA DI VIEWS
Setelah fungsi-fungsi tersebut dibuat, tambahkan path url fungsi yang ditambahkan ke dalam `urlpatterns` yang ada di `urls.py` pada direktori `main` agar fungsi tersebut dapat diakses.
```
from django.urls import path
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id 

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
]
```

## MENGAKSES URL DENGAN POSTMAN
<img width="407" alt="1" src="https://github.com/slmnrl/salmathlon/assets/124946381/60b601d6-2741-46b9-b4ee-dc2f4f140d56">
<img width="408" alt="2" src="https://github.com/slmnrl/salmathlon/assets/124946381/314d9c8d-8154-4e81-bcdc-95e86f02591a">
<img width="420" alt="3" src="https://github.com/slmnrl/salmathlon/assets/124946381/49abd4a9-973c-43db-a7f1-011f18ea135c">
<img width="421" alt="4" src="https://github.com/slmnrl/salmathlon/assets/124946381/19486b5e-2980-42e3-9888-4acd82df9fc6">
<img width="629" alt="5" src="https://github.com/slmnrl/salmathlon/assets/124946381/9f0deb04-ffde-4c44-b0fc-7daf1f254287">
<img width="617" alt="6" src="https://github.com/slmnrl/salmathlon/assets/124946381/8dc60dfb-f7f0-4b1e-a4f2-26678a2c3584">
<img width="617" alt="7" src="https://github.com/slmnrl/salmathlon/assets/124946381/9e1c5226-f52f-4139-90a6-4ccc182cfd7e">
<img width="620" alt="8" src="https://github.com/slmnrl/salmathlon/assets/124946381/df4363c0-8ad5-4100-884f-b3519c2a489d">
