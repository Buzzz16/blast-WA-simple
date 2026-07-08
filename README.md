# WhatsApp Auto-Sender Bot

Bot otomatisasi WhatsApp Web untuk mengirim pesan teks dan gambar secara massal berdasarkan data dari Excel. Proyek ini cocok untuk kebutuhan blast pesan acara, undangan, pengumuman, atau reminder.

## Fitur Utama
- Membaca nama dan nomor tujuan dari file Excel.
- Mendukung pengiriman lebih dari satu gambar sekaligus.
- Menjaga format pesan tetap rapi, termasuk emoji dan paragraf panjang.
- Membersihkan format nomor telepon yang sering berubah saat dibaca Excel.
- Mengirim pesan dengan alur otomatis lewat WhatsApp Web.

## Persyaratan Sistem
- Windows direkomendasikan, terutama jika memakai clipboard gambar sistem.
- Python 3.8 atau lebih baru.
- Google Chrome atau browser Chromium yang kompatibel.
- Koneksi internet stabil.

## Struktur Folder
Pastikan proyek tersusun seperti berikut:

```text
d:\reunusa\
├── bot_wa.py
├── README.md
├── requirements.txt
├── gambar\
│   ├── poster_1.jpg
│   └── rundown.png
├── nomerTelpon\
│   └── NomerTelpon.xlsx
└── wa_session\
```

## Instalasi
1. Buka Terminal atau PowerShell.
2. Masuk ke folder proyek:

```bash
cd d:\reunusa
```

3. Buat virtual environment dan aktifkan:

```bash
python -m venv .venv
.venv\Scripts\activate
```

4. Pasang dependensi:

```bash
pip install -r requirements.txt
```

## Persiapan Data Excel
Siapkan file `NomerTelpon.xlsx` di folder `nomerTelpon`.

Format kolom yang disarankan:
- Kolom A: Nama penerima.
- Kolom B: Nomor WhatsApp tujuan, tanpa tanda `+`, misalnya `6281234567890`.

Contoh:

| Nama | Nomor Telepon |
| --- | --- |
| Ucup | 6281365645656 |
| Udin | 6285656322222 |

Catatan: baris pertama dianggap header.

## Cara Menjalankan Bot
1. Pastikan data Excel dan gambar sudah siap.
2. Jalankan bot:

```bash
python bot_wa.py
```

3. Saat pertama kali dijalankan, scan QR Code WhatsApp Web dari ponsel.
4. Setelah login berhasil, bot akan menjalankan proses kirim otomatis.

## Session dan Data
- Folder `wa_session/` menyimpan sesi login browser.
- Jangan hapus folder ini jika ingin tetap login.
- Jika ingin login ulang, hapus folder session lalu jalankan lagi.

## Troubleshooting
- Gagal membaca Excel: pastikan nama file tepat dan file tidak sedang dibuka.
- Tidak ada gambar ditemukan: pastikan file ada di folder `gambar` dan berformat `.png`, `.jpg`, atau `.jpeg`.
- QR tidak muncul: pastikan browser dan driver kompatibel.
- Error clipboard: gunakan Windows jika proyek mengandalkan clipboard gambar sistem.

## Keamanan
- Jangan upload `wa_session/` ke repository publik.
- Simpan kredensial di environment variable jika memang dibutuhkan.
- Pastikan data nomor telepon hanya dipakai untuk kebutuhan yang sah.

## Bantuan
Jika ingin, Anda bisa kirim isi `bot_wa.py` agar README ini bisa saya sesuaikan lebih spesifik dengan alur aplikasi yang benar-benar dipakai.
