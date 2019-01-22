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
  - [x] Implementasi tampilan Dashboard *(14 Januari 2019)*
    - [x] Menampilkan informasi aplikasi
    - [x] Menampilkan daftar sektor
    - [x] Menampilkan daftar perusahaan
  - [x] Implementasi tampilan Analisis Kinerja Keuangan Perusahaan *(11 - 14 Januari 2019)*
    - [x] Membuat select form untuk memilih 1 perusahaan untuk dianalisis
    - [x] Menampilkan data financial performance variable
    - [x] Menampilkan data ratio hasil analisis
    - [x] Memberikan batasan dan keputusan terhadap hasil analisis
  - [x] Implementasi tampilan Perbandingan kinerja keuangan perusahaan *(13 - 14 Januari 2019)*
    - [x] Membuat multiselect form untuk memilih 2 perusahaan atau lebih untuk dibandingkan
    - [x] Menampilkan data rasio hasil perbandingan dalam bentuk diagram batang
    - [x] Memberikan ambang batasan (*threshold*) ratio untuk setiap diagram
  - [ ] Implementasi Real Data *()*
    - [ ] Menambahkan data sektor, perusahaan dan laporan keuangan
    - [ ] Menambahkan data nilai batasan pada analisis dan perbandingan
    - [ ] Menambahkan konten informasi pada tampilan Dashboard

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
<p align="justify">Kebutuhan fungsionalitas pada aplikasi ini berupa analisis kinerja keuangan perusahaan yang dapat menunjukkan kepada para investor perusahaan mana saja yang bisa dilakukan investasi ke depannya. Analisis kinerja keuangan yang digunakan terdiri dari dua tipe yaitu kinerja keuangan secara individu perusahaan dan perbandingan kinerja keuangan antar perusahaan. Jadi, untuk fitur utama pada web ini ada 2 yaitu fitur Kinerja Perusahaan dan fitur Perbandingan Kinerja antar Perusahaan. Pada fitur Kinerja Perusahaan, ada kolom pencarian untuk mencari perusahaan berdasarkan nama/kode/sektor perusahaannya. Pada fitur ini juga ada informasi berupa nilai dari 18 variabel perhitungan kinerja perusahaan berdasarkan perusahaan yang sudah dipilih pada kolom perusahaan sebelumnya. Selain berguna untuk informasi, ke-18 variabel juga berguna untuk perhitungan kinerja perusahaan yang bisa dibagi lagi menjadi 5 Rasio, yaitu Liquidity Ratio, Solvability Ratio, Profitability Ratio, Market Ratio dan Turnover Ratio. Pada fitur ini juga tersedia tombol untuk memulai proses perhitungan kinerja perusahaan. Setelah tombol “Proses” ditekan, maka hasil perhitungan kinerjanya bisa dilihat pada kolom 5 rasio yang sudah disebutkan tadi. Hasil perhitungannya berupa angka dan indikator warna hijau dan warna merah. Warna hijau untuk hasil yang bagus dan warna merah untuk hasil yang tidak bagus. Penentuan warna ditentukan berdasarkan batas angka pada setiap perhitungan rasionya.</p>
Berikut adalah batas angka pada setiap perhitungan rasio :

1. **Liquidity Ratio**. Angka yang dianggap baik adalah angka yang lebih dari 100%.
2. **Solvability Ratio**
   - **Debt to Asset**. Angka yang dianggap baik adalah angka yang kurang dari 100%.
   - **Debt to Equity**. Angka yang dianggap baik adalah angka yang kurang dari 100%.
   - **Long Term Debt to Equity**. Angka yang dianggap baik adalah angka yang kurang dari 100%.
   - **Coverage Ratio**. Angka yang dianggap baik adalah angka yang kurang dari 150%.
3. **Profitability Ratio**
   - **Return On Equity**. Angka yang dianggap baik adalah angka yang lebih dari 13%.
   - **Return On Asset**. Angka yang dianggap baik adalah angka yang lebih dari 5%.
   - **Gross Profit Margin**. Angka yang dianggap baik adalah angka yang lebih dari 50%.
   - **Operating Profit Margin**. Angka yang dianggap baik adalah angka yang lebih dari 30%.
   - **Net Profit Margin**. Angka yang dianggap baik adalah angka yang lebih dari 10%.
4. **Market Ratio**
   - **Price Earning Ratio**. Jika kurang dari 15 dikatakan “Cheap” dan lebih dari 15 dikatakan “Expensive”.
   - **Price to Book Value**. Nilai 1.0 adalah ambang batasnya, yang berarti jika kurang dari 1.0 maka disebut “Undervalued” sedangkan  lebih dari 1.0 disebut “Overvalued”.
   - **Dividend Yield**. Semakin besar nilai Dividend Yield maka semakin baik. Kemudian, apabila nilai tersebut ada pertumbuhan dari nilai pada tahun sebelumnya maka dapat dikatakan baik/bagus. Jadi, bagus atau tidaknya tergantung pada pertumbuhannya.Tapi pada web ini bisa disimpulkan bahwa apabila < 3% dikatakan tidak bagus dan > 3% dikatakan bagus.
   - **Dividend Payout Ratio**. Angka yang dianggap baik adalah angka yang lebih dari 50%.

<p align="justify">Selain fitur kinerja perusahaan, pada web ini juga terdapat fitur perbandingan. Perbandingan di sini adalah perbandingan kinerja antar perusahaan, mana yang memiliki kinerja yang baik dan mana yang memiliki kinerja yang buruk. Pada fitur ini terdapat kolom perusahaan yang akan dibandingkan. Berbeda dengan fitur sebelumnya, pada fitur ini hanya terdapat 11 variabel. Kemudian, variabel tersebut akan menghasilkan beberapa rasio, seperti Current Ratio, Debt to Equity Ratio, Return on Equity, Operating Profit Margin, Net Profit Margin, Price Earning Ratio, dan Dividend Yield. Rasio-rasio tersebut akan berupa grafik batang dengan ambang batas dan warna indikator sama seperti pada fitur sebelumnya. Arti dari warna indikator juga sama seperti pada fitur sebelumnya yaitu, warna merah untuk hasil yang kurang dari ambang batas berarti tidak bagus dan warna hijau untuk hasil lebih dari ambang batas berarti bagus. Kemudian, untuk menentukan bagus tidaknya digunakan perhitungan seperti yang sudah dijelaskan di atas. Setiap perusahaan yang dibandingkan memiliki hasil rasio dan warna indikatornya masing-masing dan dari grafik dan warna indikator pengguna bisa menyimpulkan bahwa perusahaan mana yang lebih baik kinerjanya. </p>
<p align="justify"> Selain kedua fitur di atas, pada sistem ini juga diberikan informasi perusahaan terkait data perusahaan agar pengguna dapat melihat perusahaan yang akan dipilih untuk berinvestasi secara mendalam. Datanya berupa deskripsi perusahaan yang terdaftar pada sistem ini.</p>

<h3 id="interface_design">Desain Antarmuka</h3>

- Dashboard Awal
<p align="center">
  <img src="https://github.com/SMTI-08/cake-web-app/blob/master/static/image/Dashboard Awal 2.png">
</p>

- Dashboard Company
<p align="center">
  <img src="https://github.com/SMTI-08/cake-web-app/blob/master/static/image/Dashboard Company 4.png">
</p>

- Dashboard Sector
<p align="center">
  <img src="https://github.com/SMTI-08/cake-web-app/blob/master/static/image/Dashboard Sector 4.png">
</p>

- Financial Performance (Before Click)
<p align="center">
  <img src="https://github.com/SMTI-08/cake-web-app/blob/master/static/image/Financial Performance (before click).png">
</p>

- Financial Performance  (After Click)
<p align="center">
  <img src="https://github.com/SMTI-08/cake-web-app/blob/master/static/image/Financial Performance (after click).png">
</p>

- Comparison Financial Performance (Before Click)
<p align="center">
  <img src="https://github.com/SMTI-08/cake-web-app/blob/master/static/image/Comparison Financial Performance 3 (2)  (Before Click).png">
</p>

- Comparison Financial Performance (After Click)
<p align="center">
  <img src="https://github.com/SMTI-08/cake-web-app/blob/master/static/image/Comparison Financial Performance 3 (2) (After Click).png">
</p>

- Help
<p align="center">
  <img src="https://github.com/SMTI-08/cake-web-app/blob/master/static/image/Help.png">
</p>

<h3 id="database_design">Desain Database</h3>
<p align="center">
  <img src="https://github.com/SMTI-08/cake-web-app/blob/master/static/image/db design.JPG">
</p>

<h3 id="implementation">Implementsi</h3>

<h3 id="testing">Pengujian</h3>
