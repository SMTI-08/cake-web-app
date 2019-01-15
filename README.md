# Cake

<p align="center">
  <img width="460" height="300" src="https://github.com/SMTI-08/cake-web-app/blob/master/static/image/cake.png">
</p>

Berikut adalah daftar rincian dokumentasi singkat dari proyek CAKe berbasis Web :
- <a href=#description>Deskripsi</a></li>
- <a href=#todo>Daftar Pekerjaan</a></li>
- <a href=#project_timeline>Timeline Pengerjaan Proyek</a></li>
- <a href=#budget_plan>Rencana Anggaran Biaya</a></li>
- <a href=#functional_analysis>Analisis Fungsionalitas</a></li>
- <a href=#interface_design>Desain Antarmuka</a></li>
- <a href=#database_design>Desain Database</a></li>
- <a href=#implementation>Implementsi</a></li>
- <a href=#testing>Pengujian</a></li> 

<h3 id="description">Deskripsi</h3>
<p align="justify">Cake merupakan suatu wadah dalam bentuk aplikasi web untuk membantu para investor melakukan analisis untuk mengambil keputusan dalam menanamkan modal disuatu saham perusahaan. Aplikasi ini ditujukan untuk user yang berperan sebagai investor saham jangka panjang. Fitur utama pada aplikasi ini adalah analisis dengan menggunakan salah satu metode analisis fundamental yaitu analisis kinerja keuangan tahunan. Analisis kinerja keuangan terdiri dari dua tipe yaitu analisis kinerja keuangan secara individu perusahaan dan analisis perbandingan kinerja keuangan antar perusahaan. Data yang digunakan pada aplikasi ini berasal dari laporan keuangan tahunan 45 perusahaan di Indonesia yang masuk daftar indeks LQ45 dari sembilan sektor.</p>

<h3 id="todo">Daftar Pekerjaan</h3>

*(14 Desember - 20 Desember 2018)*
- [x] Diskusi dengan stakeholder

*(21 Desember - 27 Desember 2018)*
- [x] Membuat analasis kebutuhan berdasarkan hasil diskusi dengan stakeholder, berupa analisis fungsional, nonfungsional, dan data
- [x] Merancang timeline pengerjaan proyek
- [x] Membuat Matriks RACI
- [x] Membuat Rencana Anggaran Biaya proyek

*(28 Desember 2018 - 17 Januari 2019)*
- Desain
  - [x] Membuat design database *(28 Desember 2018 - 5 Januari 2019)*
  - [x] Membuat design interface :
    - [x] Dashboard *(9 - 14 Januari 2019)*
    - [x] Analisis Kinerja Keuangan Perusahaan *(9 - 14 Januari 2019)*
    - [x] Perbandingan kinerja keuangan perusahaan *(9 - 14 Januari 2019)*

- Implementasi
  - [x] Membuat *environment (1 Januari 2019)* 
  - [x] Membuat *project (1 Januari 2019)*
  - [x] Membuat aplikasi *(1 Januari 2019)*
  - [x] *Setting application* ke *project (1 Januari 2019)*
  - [x] Membuat database *(3 - 5 Januari 2019)*
  - [x] Membuat fungsi untuk perhitungan *financial performance ratio (6 Januari 2019)*
  - [x] Membuat fungsi untuk menampikan data *(8 Januari 2019)*
  - [ ] Implementasi tampilan Dashboard *(14 Januari 2019)*
    - [ ] Menampilkan informasi aplikasi
    - [ ] Menampilkan daftar sektor
    - [ ] Menampilkan daftar perusahaan
  - [ ] Implementasi tampilan Analisis Kinerja Keuangan Perusahaan *(11 - 14 Januari 2019)*
    - [ ] Membuat select form untuk memilih 1 perusahaan untuk dianalisis
    - [ ] Menampilkan data financial performance variable
    - [ ] Menampilkan data ratio hasil analisis
    - [ ] Memberikan batasan dan keputusan terhadap hasil analisis
  - [ ] Implementasi tampilan Perbandingan kinerja keuangan perusahaan *(13 - 14 Januari 2019)*
    - [ ] Membuat multiselect form untuk memilih 2 perusahaan atau lebih untuk dibandingkan
    - [ ] Menampilkan data rasio hasil perbandingan dalam bentuk diagram batang
    - [ ] Memberikan ambang batasan (*threshold*) ratio untuk setiap diagram

<h3 id="project_timeline">Timeline Pengerjaan Proyek</h3>
<p align="center">
  <img src="https://github.com/SMTI-08/cake-web-app/blob/master/static/image/timeline cake.JPG">
</p>

Keterangan :
- Diskusi dengan Stakeholder. Pada tahap ini dilakukan wawancara dengan stakeholder untuk mengetahui tujuan dan keinginan stakeholder terhadap sistem yang akan dikembangkan.
- Riset Pemilihan Metode RAD. Pada tahap ini dilakukan riset untuk memutuskan metode yang tepat untuk pengembangan sistem. Pemilihan metode didasarkan pada data-data yang dihasilkan pada tahap diskuis dengan stakeholder.
- Analisis Kebutuhan. Pada tahap ini dilakukan analisis terhadap kebutuhan dalam pengembangan sistem berdasarkan data yang dihasilkan dari hasil diskusi dengan stakeholder.
- Desain. Pada tahap ini dilakukan perancangan terhadap sistem yang akan dikembangkan berdasarkan hasil tahap analisis kebutuhan. Perancangan dilakukan terhadap desain UI/UX dan desain Database.
Implementasi. Pada tahap ini dilakukan implementasi dan testing terhadap sistem berdasarkan hasil dari tahap desain ke dalam pembuatan kode.
- Deployment. Pada tahap ini dilakukan penyebaran sistem yang sudah jadi menggunakan layanan hosting dan dilakukan training terhadap stakeholder mengenai penggunakan sistem.
- Evaluasi. Tahap terakhir adalah melakukan evaluasi terhadap testing yang telah dilakukan guna mengetahui apakah aplikasi yang dibuat berjalan sesuai fungsinya dan memenuhi keinginan dari stakeholder.

<h4>Rincian Timeline Pengerjaan Proyek</h4>
<p align="center">
  <img src="https://github.com/SMTI-08/cake-web-app/blob/master/static/image/rincian kegiatan.JPG">
</p>

<h4>Matriks RACI</h4>
<p align="center">
  <img src="https://github.com/SMTI-08/cake-web-app/blob/master/static/image/RACI Matrix.JPG">
</p>

Keterangan :
- R = Responsible. Pihak yang bertanggung jawab untuk mengerjakan  aktivitas tersebut.
- A = Accountable. Pihak yang bertanggung jawab untuk memastikan penyelesaian pekerjaan dan menyetujui hasil suatu pekerjaan.
- C = Consulted. Pihak yang dimintai saran dan pendapat tentang suatu pekerjaan yang sedang dikerjakan.
- I = Informed. Pihak yang akan diinformasikan terhadap perkembangan terbaru dari suatu pekerjaan.

<h3 id="budget_plan">Rencana Anggaran Biaya</h3>
<p align="center">
  <img src="https://github.com/SMTI-08/cake-web-app/blob/master/static/image/Anggaran1.JPG">
</p>
<p align="center">
  <img src="https://github.com/SMTI-08/cake-web-app/blob/master/static/image/Anggaran2.JPG">
</p>

<h3 id="functional_analysis">Analisis Fungsionalitas</h3>

<h3 id="interface_design">Desain Antarmuka</h3>

<h3 id="database_design">Desain Database</h3>

<h3 id="implementation">Implementsi</h3>

<h3 id="testing">Pengujian</h3>
