Link PWS = https://naufal-fadli41-goatsports.pbp.cs.ui.ac.id/

TUGAS INDIVIDU 2

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
= buat direktori kemudian aktifkan virtual environment. Setelah itu install dependencies yang dibutuhkan dilanjutkan dengan instalasi projek djangonya. Atur berkas .env dan .env.prod. Selanjutnya modifikasi file settings.py untuk menggunakan environment variables. pada settings.py tambahkan host pada ALLOWED_HOST, atur konfigurasi PRODUCTION dan ubah konfigurasi DATABASE. Selanjutnya migrasi database. Kemudian keluar dari virtual environment dan buat repo github untuk projek kita. Lacak perubahan file pada direktori projek dengan melakukan git init. Tambahnkan berkas .gitignore. hubungkan direktori lokal dengan repo github dan buat branch utama master. lakukan add, commit, dan push. Lanjut dengan membuat aplikasi main dengan menjalankan command untuk membuat aplikasi main (python manage.py startapp main). tambahkan main kedalam INSTALLED_APPS pada settings.py. Lanjut untuk membuat template, buat direktori template pada direktori aplikasi main yang berisi berkas main.html. lanjut lakukan implementasi model dengan mengubah models.py pada direktori aplikasi main. lakukan migrasi model.hubungkan views.py dengan main.html(template) dengan menambah baris import serta fungsi show_main pada views.py. Ubah nama dan kelas menjadi struktur kode Django pada main.html. Sleanjutnya konfigurasi routing pada main dan proyek  dengan menambahkan urls.py pada direktori main dan direktori utama(GoatSport). Deploy ke PWS dengan create new project, kemudian edit environ sesuai dgn isi file dari .env.prod.. tambahkan ALLOWED_HOSTS berupa url deployment. Jalankan command yang ada pada project command. jika sudah maka push ke pws. buat README.md kemudian tambahkan ke direktori utama.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
= <img width="2876" height="1521" alt="image" src="https://github.com/user-attachments/assets/50db5e95-9ae1-4192-809d-f5dd62915de7" />
urls.py berisi url yang akan dicocokkan dengan input client, jika cocok akan  ditampilkan view.py pada aplikasi yang cocok. view.py akan mengambil atau meproses data dari model jika diperlukan. view.py kemudian akan ditampilkan kepada pengguna melalui template

4. Jelaskan peran settings.py dalam proyek Django!
= settings.py berperan untuk mengatur konfigurasi pada proyek django kita, mulai dari database, host, installed apps, dll.

5. Bagaimana cara kerja migrasi database di Django?
= dengan menciptakan berkas migrasi yang berisi perubahan model yang belum diaplikasikan ke dalam basis data, kemudian mengaplikasikan perubahan model yang tercantum dalam berkas migrasi ke basis data dengan menjalankan perintah sebelumnya.

6. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
= karena django menggunakan python yang notabene adlaah bahasa pemrograman yang cukup mudah untuk dipahami. Komunitas yang besar juga akan sangat membantu kita dalam mempelajari django untuk pengembangan perangkat lunak

7. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
= Sejauh ini tidak, asdos sangat membantu dalam mengatasi masalah saat tutorial.


TUGAS INDIVIDU 3

1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
= data delivery penting dalam sebuah platform agar kita dapat mendistribusikan data dari satu lokasi dengan akurat, konsisten, dan lebih efisien ke lokasi yang lain.

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
= Menurut saya JSON, karena JSON memiliki syntaks yang lebih simpe dan compact, serta merupakan turunan langsung dari JavaScript object literal syntax sehingga mudah digunakan dalam environments JavaScript.

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
= fungsi dari method ini adalah untuk melakukan validasi dan juga cleaning pada data yang disubmit. Validasi dapat berupa max_length pada atribut name proyek ini. kita membutuhkkan is_valid() ini untuk mencegah data yang invalid serta mendapatkan data yang sudah bersih melalui proses cleaned_data.

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
= kita membutuhkan csrf_token untuk membuat token yang unik dan kemudian akan dicek oleh server untuk setipa request yang mengubah suatu state. jika tooken invalid maka request akan ditolak. Jika tidak menambahkan csrf_token, akan terjadi kerentanan pada situs dimana penyerang akan menyamar menjadi korban dengan cara membuat halaman eksternal yang mengirim POST otomatis ke endpoint aplikasi korban. Hal ini terjadi karena browser akan menyertakan cookie otentikasi user. Penyerang kemudian dapat mengubah password user pada situs tersebut ataupun atribut lain yang dimiliki oleh user, karena situs menganggap penyerang adalah user.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
= buat direktori template pada folder, kemudian isi dengan base.html yang akan berperan sebagai template dasar untuk halaman web lain dalam proyek. Pada setting.py tambahkan base.html sebagai berkas template. Buat berkas forms.py pada direktori main untuk menerima data input produk. Tambahkan fungsi create_product dan show_product pada views.py unutk membuat dan memperlihatkan product. import fungsi create_product dan show_product pada urls.py dan tambahkan path masing-masing. modifikasi main.html untuk menyesuaikan dengan template, menambah button untuk add product dan menampilkan product yang tersedia. Buat berkas create_product.html dan product_detail.html pada direktori main/templates unutk menampilkan form input dan menampilkan product. Tambahkan link deployment pws pada settings.py bagian CSRF_TRUSTED_ORIGINS. Import HttpResponse dan serializers pada views.py untuk digunakan pada fungsi show_xml, show_json, show_xml_by_id, show_json_by_id. Tambah fungsi show_xml, show_json, show_xml_by_id, show_json_by_id pada views.py, kemudian import fungsi-fungsi ini ke urls.py dan tambahkan path untuk masing-masing fungsi.

6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
= sejauh ini tidak ada

Screenshot postman :
<img width="2574" height="1041" alt="Cuplikan layar 2025-09-17 085451" src="https://github.com/user-attachments/assets/1acd2a82-ed29-4ef0-be1e-db5e4e880f42" />
<img width="2591" height="987" alt="Cuplikan layar 2025-09-17 085432" src="https://github.com/user-attachments/assets/d97c9559-2203-4304-8b8b-a3a318bd77ea" />
<img width="2597" height="1083" alt="Cuplikan layar 2025-09-17 085123" src="https://github.com/user-attachments/assets/291493f2-fed0-4434-bb60-4412f27c8d35" />
<img width="2601" height="1005" alt="Cuplikan layar 2025-09-17 085103" src="https://github.com/user-attachments/assets/4a9c1ef5-0cd0-4fae-b6fe-69357ecafd14" />


TUGAS INDIVIDU 4

1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
= merupakan form autentikasi bawaan dari Django yang mempunyai fungsi untuk melakukan proses autentikasi login pengguna. Kelebihannya adalah kita cukup memakai form bawaan ini tanpa perlu melakukan implementasi ulang kode untuk autentikasi login pengguna dan terintegrasi langsung dengan sistem session dan user Django., sehingga kode lebih efisien dan ringkas. Kekurangannya adalah opsi untuk melakukan login hanya terbats pada username dan password user, Kurang fleksibel untuk multi-factor authentication seperti kode OTP dan Captcha.

2. Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
= Autentikasi adalah tahapan dalam memverifikasi identitas seseorang apakah sesuai atau tidak. Otorisasi adalah tahapan menentukan hak akses yang dimiliki oleh suatu user. Implementasi autentikasi dilakukan dengan AuthenticationForm serta django.contrib.auth import login dan logout. Implementasi otorisasi dapat menggunakan decorator @login_required atau bisa juga dengan @permission_required('app_name.change_model').

3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
= Session 
- Kelebihan = Lebih aman untuk data sensitif karrena data disimpan pada server, lebih fleksibel karena bisa menyimpan daat kompleks.
- Kekurangan = Membebani kinerja server, akan expired apabila browser ditutup

Cookies 
- Kelebihan = Mudah diakses oleh client, tidak membebani server karena data disimpan pada browser user, bisa dilakukan set agar expirednya lama.
- Kekurangan = Kapasitas terbatas, rentan terhadap XSS.

4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
= Secara default tidak, karena ada resiko potensial berupa XSS, hal ini bisa diatasi jika kita memberikan atribut HttpOnly. Ada juga CSRF yang dapat diatasi dengan CSRF token yang dapat digunakan di form POST.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
= Untuk fitur register, pada views.py Import UserCreationForm dan messages, Tambah fungsi register. Pada direktori main/templates tambah berkas register.html. Pada urls.py lakukan import fungsi register dan tambah path urlnya. 

Untuk fitur login, pada views.py Import authenticate, login, dan AuthenticationForm, kemudian tambah fungsi login_user. Pada direktori main/templates tambah berkas login.html. Pada urls.py lakukan import fungsi login_user dan tambah path urlnya. 

Untuk fitur logout, pada views.py Import logout, kemudian tambah fungsi logout_user. Pada direktori main/templates tambah berkas login.html. Pada urls.py lakukan import fungsi logout_user dan tambah path urlnya.

Untuk merestriksi akses ke halaman main dan product detail, import login_required pada views.py. Tambahkan potongan kode @login_required(login_url='/login') untuk mengaplikasikan decorator login_required, diatas fungsi show_main dan juga show_news.

Untuk mengakses data dari cookie, Tambahkan import HttpResponseRedirect, reverse, dan datetime pada views.py. Modifikasi fungsi login_user agar bisa menyimpan cookie last_login. Pada fungsi show_main, lakukan penambahan kode 'last_login'. Pada fungsi logout_user, lakukan penambahan kode untuk menghapus cookie last_login. Pindah ke main.html pada main/templates dan lakukan penambahan kode untuk menampilkan waktu terakhir login.

Untuk menghubungkan model news dengan user, import user pada models.pydan tambahkan kode "user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)". Lanjutkan dengan melakukan migrate model. Pindah ke views.py pada main, modifikasi kode yang ada pada fungsi create_product. Lakukan juga modifikasi kode pada fungsi show_main. Pindah ke main.html di main/templates dan tambahkan tombol filter My dan All. Pindah ke product_detail.html di main/templates kemudian tambahkan kode untuk menampilkan nama seller(penjual). Kemudian buat 2 akun pengguna (saya pilih adidas dan nike) dengan masing-masing 3 dummy data.


TUGAS INDIVIDU 5

1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
= Jika terdapat beberapa CSS selector untuk suatu elemen HTML, maka style yang akan diterapkan adalah yang memiliki prioritas yang lebih tinggi. Urutan dari CSS selector yang memiliki prioritas paling tinggi adalah sebagai berikut : Inline styles, ID selectors, Classes selector, Element selector.


2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!
= Responsive design penting karena pengguna dapat mengakses web kita dari berbagai device. Tanpa responsive design, design web kita akan berantakan ketika dibuka dari device lain. Contoh dari web yang sudah menerapkan responsive design adalah web steam dimana hal ini membuat user dapat melakukan pembelian game di steam tanpa perlu mengakses komputer/laptop, tapi bisa lewat handphone, tablet, atau steamdeck. Contoh web yang tidak menerapkan responsive design adalah web yang dikelola pemerintah. Hal ini karena umumnya website yang dikelola pemerintah ini sudah ada sejak lama dan enggan dilakukan pembaruan karna dirasa kurang penting.

3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
= Padding merupakan area kosong(transparan) yang menjadi jarak antara konten elemen dengan border. Border merupakan garis tepian yang membungkus konten dan juga padding. Margin merupakan area kosong(transparan) yang menjadi jarak antara bagian konten dengan border. Contoh pengaplikasiannya : 
div {
  width: 300px;
  border: 15px solid green;
  padding: 50px;
  margin: 20px;
}

4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
=Flexbox adalah layout method untuk mengatur item dalam satu dimensi (baris atau kolom). Kegunaannya adalah untuk menyusun item agar rata tengah (horizontal & vertical alignment), membuat layout responsif sederhana, membagi ruang antar elemen.

Grid Layout adalah layout method untuk mengatur item dalam dua dimensi (baris dan kolom). Kegunaannya adalah untuk mendesain halaman kompleks (header, sidebar, main, footer)dan membagi halaman ke dalam area grid yang rapi.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
= Karena saya menggunakan tailwind, lakukan penambahan tailwind ke aplikasi dengan menggunakan CDN dari tailwind. Untuk fitur edit dan delete product, lakukan penambahan fungsi edit_product dan delete_product pada  views.py. Kemudian buat berkas baru edit_news.html pada main/templates. Lanjutkan dengan mengimport kedua fungsi tersebut ke urls.py dan tambahkan pathnya masing-masing. Selanjutnya imlementasi fitur navigation bar dengan membuat berkas baru bernama navbar.html di folder templates/ pada root direktori dan tautkan ke dalam main.html di direktori main/templates/ dengan tag include. Tahap selanjutnya adalah mengonfigurasi static files pada settings.py di direktori goat_sports/ dengan menambahkan middleware dan mengonfigurasi  variabel STATIC_ROOT, STATICFILES_DIRS, dan STATIC_URL. Tahap selanjutnya adalah styling aplikasi. Pertama buat file global.css di direktori static/css/, hubungkan global.css dan script Tailwind ke base.html, tambahkan custom styling ke global.css. Setelah itu lakukan modifikasi styling pada navbar.html, login.html, register.html, product_detail.html, create_product.html, edit_product.html. Buat file baru card_product.html untuk mengimplementasikan elemen card untuk product.


