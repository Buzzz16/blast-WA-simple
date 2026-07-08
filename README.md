
# 🤖 WhatsApp Auto-Sender Bot (Excel & Image Support) 🚀

Bot otomatisasi WhatsApp Web menggunakan **Selenium** dan **Python**. Skrip ini dirancang khusus untuk mengirimkan gambar secara massal beserta pesan teks dinamis (menyebut nama penerima) yang datanya diambil langsung dari file Excel.

Sangat cocok untuk keperluan *blast* pesan acara, undangan, atau *reminder* (seperti acara Reunusa) tanpa perlu repot melakukan *copy-paste* satu per satu secara manual.

---

## 🌟 Fitur Utama
* **Data Dinamis dari Excel**: Membaca nama dan nomor tujuan secara otomatis dari file `.xlsx`.
* **Multi-Image Support**: Mendukung pengiriman lebih dari satu gambar sekaligus (PNG/JPG/JPEG).
* **Bypass Limitasi Teks & Emoji**: Menggunakan metode *clipboard copy-paste* sehingga emoji dan format paragraf panjang tetap rapi.
* **Auto-Clean Number**: Otomatis mendeteksi dan membersihkan format nomor telepon yang terbaca salah oleh Excel (misal: `628123.0`).
* **Skenario Tahan Banting**: Menggunakan simulasi tombol `ENTER` untuk mengirim, mencegah error karena perubahan kode tombol (UI) di WhatsApp Web.

---

## ⚙️ Persyaratan Sistem (Prerequisites)

Sebelum menjalankan bot ini, pastikan sistem kamu memenuhi syarat berikut:
1. **OS Windows**: Wajib menggunakan Windows karena skrip ini menggunakan `win32clipboard` untuk mengatur *clipboard* gambar sistem.
2. **Python 3.8+**: Pastikan Python sudah terinstal dan ditambahkan ke *PATH* environment.
3. **Google Chrome**: Browser Chrome harus terinstal di komputer.

---

## 📂 Struktur Folder
Pastikan direktori atau folder kamu disusun seperti ini agar skrip berjalan lancar tanpa error *Path Not Found*:

```text
D:\reunusa\
│
├── gambar\                   # Masukkan SEMUA foto yang ingin dikirim ke sini (.png/.jpg)
│   ├── poster_1.jpg
│   └── rundown.png
│
├── nomerTelpon\              # Folder untuk menyimpan database nomor telepon
│   └── NomerTelpon.xlsx
│
├── bot_wa.py                 # File utama script Python
└── requirements.txt          # File list library Python

```

---

## 🛠️ Cara Instalasi

1. Buka **Terminal** atau **Command Prompt** (CMD).
2. Arahkan ke folder proyek:
```bash
cd D:\reunusa\

```


3. Instal semua pustaka (*library*) yang dibutuhkan dengan perintah:
```bash
pip install -r requirements.txt

```



---

## 📝 Persiapan Data Excel

Siapkan file `NomerTelpon.xlsx` di dalam folder `nomerTelpon`.
**Aturan pengisian kolom:**

* **Kolom A (Kolom Pertama)**: Nama Penerima (akan dipanggil di dalam pesan).
* **Kolom B (Kolom Kedua)**: Nomor WhatsApp tujuan (wajib menggunakan kode negara tanpa tanda `+`, contoh: `628...`).

**Contoh Format Excel:**

| Nama (Kolom A) | Nomor Telepon (Kolom B) |
| --- | --- |
| ucup | 6281365645656 |
| udin | 6285656322222 |

> ⚠️ **Catatan:** Baris pertama (Row 1) akan dianggap sebagai judul tabel/Header dan **tidak akan dikirimkan pesan**. Kontak pertama yang diproses adalah baris ke-2.

---

## 🚀 Cara Menjalankan Bot

1. Pastikan gambar sudah siap di folder `gambar` dan Excel sudah terisi.
2. Buka Terminal/CMD di folder `D:\reunusa\`.
3. Jalankan skrip dengan perintah:
```bash
python bot_wa.py

```


4. **Scan QR Code:** Saat browser Chrome terbuka untuk pertama kalinya, kamu memiliki waktu sekitar 60 detik untuk melakukan *Scan QR Code* menggunakan aplikasi WhatsApp di HP kamu.
5. Setelah *login* berhasil, bot akan mulai bekerja secara otomatis. **Jangan menutup jendela browser** atau mengklik sembarangan saat bot sedang mengetik!

---

## 💡 Troubleshooting (Penyelesaian Masalah)

| Masalah | Solusi |
| --- | --- |
| **Gagal membaca Excel** | Pastikan file bernama *tepat* `NomerTelpon.xlsx` dan berada di folder `nomerTelpon`. Pastikan juga file tidak sedang dibuka di aplikasi Excel saat bot dijalankan. |
| **Tidak ada gambar ditemukan** | Pastikan ekstensi gambar adalah `.png`, `.jpg`, atau `.jpeg` dan diletakkan di dalam folder `D:\reunusa\gambar\`. |
| **WhatsApp Web Timeout** | Koneksi internet mungkin lambat. Coba perbesar angka `WebDriverWait(driver, 60)` di kode menjadi `120` jika butuh waktu lebih lama untuk *Scan QR*. |
| **Error terkait Clipboard** | Pastikan kamu menjalankan skrip ini di **OS Windows**. Pustaka `win32clipboard` tidak didukung di Mac atau Linux. |

---

