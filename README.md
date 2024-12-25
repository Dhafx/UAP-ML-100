# Klasifikasi Spesialisasi Medis Berdasarkan Transkripsi
Ujian Akhir Praktikum Machine Learning

Link Deployment = https://uap-ml-100-oeoclrtazm5ygyf2jjn8an.streamlit.app/

## Deskripsi Proyek
Proyek ini bertujuan untuk mengembangkan model klasifikasi teks yang dapat menentukan spesialisasi medis berdasarkan transkripsi. Latar belakang pengembangan ini adalah kebutuhan untuk mengotomatisasi proses identifikasi spesialisasi medis dari teks transkripsi guna mendukung efisiensi dalam pengelolaan data medis. Model yang dikembangkan diharapkan mampu membantu profesional medis dalam menganalisis dan mengelompokkan data transkripsi secara lebih cepat dan akurat.

## Langkah Instalasi

1. **Kloning Repository**
   Unduh repository dari GitHub dengan mengunjungi tautan berikut: [UAP-ML-100](https://github.com/Dhafx/UAP-ML-100) dan ekstrak file ZIP-nya.

2. **Membuat Virtual Environment**
   - Jalankan Python dan buat virtual environment dengan perintah berikut:
     - Untuk Linux/Mac: `python -m venv venv && source venv/bin/activate`
     - Untuk Windows: `python -m venv venv && venv\Scripts\activate`

3. **Instal Dependencies**
   - Pastikan virtual environment aktif, lalu jalankan perintah: `pip install -r requirements.txt`

## Deskripsi Model

Proyek ini menggunakan dua model utama:

1. **Bi-LSTM (Bidirectional Long Short-Term Memory)**
   - Arsitektur Bi-LSTM dirancang untuk menangkap hubungan dependensi dalam data teks dari kedua arah (forward dan backward).
   - Model ini dilatih menggunakan dataset [Medical Transcription Instruct](https://huggingface.co/datasets/DataFog/medical-transcription-instruct).

2. **IndoBERT**
   - Model ini adalah varian BERT yang dirancang untuk bahasa Indonesia.
   - Menggunakan transfer learning untuk memanfaatkan pengetahuan yang sudah ada dari pretraining.


## Hasil Training


## Link Live Demo

Aplikasi web yang telah di-deploy dapat diakses melalui tautan berikut: [Live Demo](#)

## Dataset
Dataset yang digunakan untuk pelatihan dan evaluasi model tersedia di [Medical Transcription Instruct](https://huggingface.co/datasets/DataFog/medical-transcription-instruct).

## Lisensi
Proyek ini dilisensikan di bawah [MIT License](LICENSE).
