# Cake

<p align="center">
  <img width="460" height="300" src="https://github.com/SMTI-08/cake-web-app/blob/master/static/image/cake.png">
</p>

Berikut adalah daftar rincian dokumentasi singkat dari proyek CAKe berbasis Web :
<ul>
  <li><a href=#description>Deskripsi</a></li>
  <li><a href=#todo>Daftar Pekerjaan</a></li>
  <li><a href=#project_timeline>Timeline Pengerjaan Proyek</a></li>
  <li><a href=#budget_plan>Rencana Anggaran Biaya</a></li>
  <li><a href=#functional_analysis>Analisis Fungsionalitas</a></li>
  <li><a href=#interface_design>Desain Antarmuka</a></li>
  <li><a href=#database_design>Desain Database</a></li>
  <li><a href=#implementation>Implementsi</a></li>
  <li><a href=#testing>Pengujian</a></li>
</ul>  

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
    - [x] Dashboard *(9 - 14 Januari)*
    - [x] Analisis Kinerja Keuangan Perusahaan *(9 - 14 Januari)*
    - [x] Perbandingan kinerja keuangan perusahaan *(9 - 14 Januari)*

- Implementasi
  - [x] Membuat *environment (1 Januari 2019)* 
  - [x] Membuat *project (1 Januari 2019)*
  - [x] Membuat aplikasi *(1 Januari 2019)*
  - [x] *Setting application* ke *project (1 Januari 2019)*
  - [x] Membuat database *(3 - 5 Januari 2019)*
  - [x] Membuat fungsi untuk perhitungan *financial performance ratio (6 Januari 2019)*
  - [x] Membuat fungsi untuk menampikan data *(8 Januari 2018)*
  - [ ] Implementasi tampilan Dashboard *()*
    - [ ] Menampilkan informasi aplikasi
    - [ ] Menampilkan daftar sektor
    - [ ] Menampilkan daftar perusahaan
  - [ ] Implementasi tampilan Analisis Kinerja Keuangan Perusahaan *()*
    - [ ] Membuat select form untuk memilih 1 perusahaan untuk dianalisis
    - [ ] Menampilkan data financial performance variable
    - [ ] Menampilkan data ratio hasil analisis
    - [ ] Memberikan batasan dan keputusan terhadap hasil analisis
  - [ ] Implementasi tampilan Perbandingan kinerja keuangan perusahaan *()*
    - [ ] Membuat multiselect form untuk memilih 2 perusahaan atau lebih untuk dibandingkan
    - [ ] Menampilkan data rasio hasil perbandingan dalam bentuk diagram batang
    - [ ] Memberikan ambang batasan (*threshold*) ratio untuk setiap diagram
