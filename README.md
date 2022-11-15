# Analisis Indeks Literasi Indonesia

Sistem analisis indeks literasi di Indonesia ini disusun untuk menyelesaikan tugas IF4070 Representasi Pengetahuan dan Penalaran. Sistem ini adalah sistem yang dapat menganalisis indeks literasi di Indonesia menggunakan model pembelajaran mesin yang dilatih dengan data pada open data indonesia.

Data yang digunakan berasal dari data Perpustakaan Nasional Indonesia dan bisa diakses dari tautan berikut ini: https://katalog.data.go.id/dataset/indeks-pembangunan-literasi-masyarakat-2021

## Kakas yang digunakan

- Python
- Jupyter Notebook

Library:
- sklearn
- gradio

## Detail Sistem

Pada repositori ini terdapat 3 file penting, berikut deskripsi dari masing-masing file:

1. **indeks_literasi_notebook.ipynb** - file ini merupakan file hasil analisis menggunakan Data Science terhadap Indeks Pembangunan Literasi Masyarakat di Indonesia
2. **model_iplm.pkl** - Model hasil latih pembelajaran mesin yang dilakukan dalam notebook
3. **app.py** - Aplikasi yang mengimplementasikan model hasil pembelajaran untuk dapat digunakan sebagai sistem prediksi Indeks Pembangunan Literasi Masyarakat di Indonesia

## Hasil

Sistem penghitungan indeks literasi sudah ter-deploy pada situs berikut ini - https://huggingface.co/spaces/leomatt547/indeks_literasi

<img src="https://github.com/alvinwilta/indeks-literasi/blob/main/indeks_literasi_app.png">
