Link PWS = https://naufal-fadli41-goatsports.pbp.cs.ui.ac.id/

Tugas 1 Individu

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


Tugas 2 Individu
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
