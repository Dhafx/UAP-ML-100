# Klasifikasi Spesialisasi Medis Berdasarkan Transkripsi
Ujian Akhir Praktikum Machine Learning

##Link Deployment = https://uap-ml-100-oeoclrtazm5ygyf2jjn8an.streamlit.app/

## Deskripsi Proyek
Proyek ini bertujuan untuk mengembangkan model klasifikasi teks yang dapat menentukan spesialisasi medis berdasarkan transkripsi. Latar belakang pengembangan ini adalah kebutuhan untuk mengotomatisasi proses identifikasi spesialisasi medis dari teks transkripsi guna mendukung efisiensi dalam pengelolaan data medis. Model yang dikembangkan diharapkan mampu membantu profesional medis dalam menganalisis dan mengelompokkan data transkripsi secara lebih cepat dan akurat.

## Langkah Instalasi

1. **Kloning Repository**
   Unduh repository dari GitHub dengan mengunjungi tautan berikut: [UAP-ML-100](https://github.com/Dhafx/UAP-ML-100) dan ekstrak file ZIP-nya.

2. **Membuat Virtual Environment**
   - Jalankan Python dan buat virtual environment 

3. **Instal Dependencies**
   - Pastikan virtual environment aktif, lalu jalankan perintah: `pip install -r requirements.txt`
     
4. **Menjalankan Aplikasi Web**
   - Jalankan aplikasi dengan perintah: `dashboard-uap.py`
  
## Dataset
Dataset yang digunakan dalam proyek ini tersedia di [Medical Transcription Instruct](https://huggingface.co/datasets/DataFog/medical-transcription-instruct). Dataset ini terdiri dari 38.924 sampel data berupa input-output instruksi, yang sangat berguna untuk melatih model yang mengikuti instruksi dalam domain medis.

Namun, untuk proyek ini, hanya digunakan 9 label dari kolom `medical_speciality` yang aslinya berjumlah 40 label. Berikut adalah label yang dipilih:

- Neurology
- Neurosurgery
- Obstetrics Gynecology
- Ophthalmology
- Orthopedic
- Pain Management
- Pediatrics Neonatal
- Radiology
- Surgery
  
## Deskripsi Model
Proyek ini menggunakan dua model utama:

1. **Bi-LSTM (Bidirectional Long Short-Term Memory)**
   - Arsitektur Bi-LSTM dirancang untuk menangkap hubungan dependensi dalam data teks dari kedua arah (forward dan backward).
   Berikut arsitektur yang dipakai :
   ![image](https://github.com/user-attachments/assets/83b5860a-b3f6-457a-a587-7cff40c57ef2)

2. **IndoBERT**
   - Model ini adalah varian BERT yang dirancang untuk bahasa Indonesia.
   - Menggunakan transfer learning untuk memanfaatkan pengetahuan yang sudah ada dari pretraining.


## Hasil Training
1. **Bi-LSTM (Bidirectional Long Short-Term Memory)**
   Grafik akurasi dan loss :
   ![image](https://github.com/user-attachments/assets/36864484-a695-46f3-931c-63a852f24ab4)


3. **IndoBERT**
   - Model ini adalah varian BERT yang dirancang untuk bahasa Indonesia.
   - Menggunakan transfer learning untuk memanfaatkan pengetahuan yang sudah ada dari pretraining.

## Link Live Demo

Aplikasi web yang telah di-deploy dapat diakses melalui tautan berikut: [Live Demo](#)


