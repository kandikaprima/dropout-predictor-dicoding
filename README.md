# Proyek Akhir: Menyelesaikan Permasalahan Jaya Jaya Institut

## Business Understanding
Jaya Jaya Institut adalah institusi pendidikan tinggi yang telah berdiri sejak tahun 2000 dan telah meluluskan banyak mahasiswa berprestasi. Namun, tingginya angka siswa yang tidak menyelesaikan pendidikan atau dropout menjadi tantangan serius bagi reputasi dan efektivitas institusi ini.

### Permasalahan Bisnis
Tingginya angka dropout di Jaya Jaya Institut berdampak pada reputasi akademik dan efektivitas institusi dalam meluluskan mahasiswa tepat waktu. Oleh karena itu, manajemen membutuhkan solusi berbasis data yang mampu mengidentifikasi siswa berisiko tinggi secara dini agar intervensi yang tepat dapat diberikan lebih awal.



### Cakupan Proyek
- Melakukan eksplorasi data dan visualisasi performa siswa.
- Membangun dashboard interaktif untuk monitoring performa siswa.
- Mengembangkan model machine learning untuk memprediksi kemungkinan siswa dropout.
- Melakukan deployment sistem prediksi menggunakan Streamlit.
- Memberikan rekomendasi actionable bagi institusi untuk mengurangi angka dropout.

### Persiapan

Sumber data: https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/README.md

Setup environment:
```
pip install -r requirements.txt
```

## Business Dashboard

Dashboard ini dibuat menggunakan Metabase yang terhubung ke database Supabase. Visualisasi meliputi:

- Distribusi status mahasiswa (Graduate, Dropout, Enrolled)
- Distribusi DO berdasarkan Debtor
- Distribusi DO per Course
- Rata-rata Admission Grade berdasarkan Status (Graduate, Dropout, Enrolled)
- Rata-rata umur siswa berdasarkan Status (Graduate, Dropout, Enrolled)
- Distribusi DO berdasarkan Gender
- Tren DO berdasarkan GDP

🔐 Login Metabase:
- Email: root@mail.com
- Password: Hara3AR0N5gQdc

## Menjalankan Sistem Machine Learning
Model prediktif dibangun menggunakan Random Forest dan dideploy menggunakan Streamlit Cloud.

🔗 Akses aplikasi prediksi:
https://dropout-predictor-dicoding-kandikaprima.streamlit.app

Cara Menjalankan Lokal:
```
streamlit run app.py
```
File model: models/dropout_rf_model.pkl

## Conclusion
Model machine learning berhasil membedakan antara siswa dropout dan non-dropout dengan akurasi yang tinggi (>88%). Berdasarkan hasil analisis, ditemukan bahwa:
- Nilai masuk yang rendah, umur pendaftaran lebih tua, dan masalah keuangan (utang, keterlambatan membayar) adalah indikator utama dropout.
- Beberapa jurusan secara signifikan memiliki angka dropout lebih tinggi dibandingkan lainnya.

### Rekomendasi Action Items
Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.
- 🎯 Gunakan sistem prediksi untuk mengidentifikasi siswa berisiko sejak awal.
- 💬 Adakan program bimbingan untuk siswa dengan admission grade rendah.
- 💸 Evaluasi kebijakan keuangan bagi mahasiswa yang sering terlambat membayar atau memiliki tunggakan.
- 📊 Pantau performa jurusan-jurusan dengan dropout tinggi untuk perbaikan kurikulum atau pendekatan pengajaran.
