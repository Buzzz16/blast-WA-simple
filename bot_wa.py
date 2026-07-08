import io
import os
import time
import glob
import pyperclip
import pandas as pd
from PIL import Image
import win32clipboard
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException

# ==========================================
# 1. FUNGSIONALITAS COPY GAMBAR KE CLIPBOARD
# ==========================================
def copy_image_to_clipboard(image_path):
    """Membuka file gambar dan menyalinnya ke Clipboard Windows."""
    image = Image.open(image_path)
    output = io.BytesIO()
    image.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]  
    output.close()

    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()

# ==========================================
# 2. KONFIGURASI DATA DARI EXCEL & FOLDER GAMBAR
# ==========================================
# Path file Excel (Sesuaikan nama folder dan file jika berbeda)
file_excel = r"D:\reunusa\nomerTelpon\NomerTelpon.xlsx"

try:
    # Membaca Excel (menganggap baris pertama adalah judul kolom/header)
    df = pd.read_excel(file_excel)
    print(f"✅ Berhasil memuat data dari Excel. Total {len(df)} kontak ditemukan.")
except Exception as e:
    print(f"❌ Gagal membaca file Excel di {file_excel}!")
    print(f"   Detail: {e}")
    exit()

# Mengambil SEMUA gambar dari folder
folder_gambar = r"D:\reunusa\gambar"
valid_extensions = ("*.png", "*.jpg", "*.jpeg")
list_gambar = []

for ext in valid_extensions:
    list_gambar.extend(glob.glob(os.path.join(folder_gambar, ext)))

if not list_gambar:
    print(f"❌ Tidak ada gambar di {folder_gambar}!")
    exit()

print(f"✅ Ditemukan {len(list_gambar)} gambar siap dikirim.")

# ==========================================
# 3. SETTING BROWSER
# ==========================================
options = webdriver.ChromeOptions()
path_session = os.path.join(os.getcwd(), "wa_session")
options.add_argument(f"--user-data-dir={path_session}")
options.add_argument("--window-size=1280,800")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

print("\nMembuka WhatsApp Web...")
driver.get("https://web.whatsapp.com")

try:
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "pane-side")))
    print("WhatsApp Web siap! Memulai pengiriman...\n")
except TimeoutException:
    print("Gagal mendeteksi halaman utama (Timeout).")
    driver.quit()
    exit()

# ==========================================
# 4. SKENARIO UTAMA (LOOP EXCEL -> KIRIM GAMBAR -> KIRIM TEKS VIA ENTER)
# ==========================================
# iterrows() digunakan untuk membaca Excel baris demi baris
for index, row in df.iterrows():
    try:
        # Mengambil Data dari Kolom A (Indeks 0) dan Kolom B (Indeks 1)
        namaPenerima = str(row.iloc[0]).strip()
        nomor_raw = str(row.iloc[1]).strip()
        
        # Bersihkan format nomor (hapus karakter desimal .0 jika terbaca sebagai float)
        nomor = nomor_raw.replace('.0', '')
        
        # Melewati baris jika kosong
        if pd.isna(row.iloc[0]) or pd.isna(row.iloc[1]) or not nomor:
            continue
            
        print(f"[{index+1}/{len(df)}] Memproses kontak: {namaPenerima} ({nomor})...")
        
        # Membuat Pesan Dinamis (f-string)
        pesan = f"""📭Sambut Reunusa (Sesi 1)📭

Assalamu'alaikum Wr. Wb. 
Halo {namaPenerima}! 👋

Hari yang ditunggu-tunggu akhirnya tiba!

Catat Waktunya (LIVE HARI INI):
📆 Hari/Tanggal: Minggu, 5 Juli 2026
⏰ 16.00-18.05
📍 Platform: Zoom Meeting

Langsung klik link di bawah ini buat langsung masuk ke ruang meeting ya:
🔗 https://us06web.zoom.us/j/83064429692?pwd=MwcTH9LdJR8HAt5dIpa3shpOU5sRbd.1

Jangan sampai kelewatan kesempatan berharga buat jalin silaturahim!

VBG: 
https://drive.google.com/file/d/1DNgcru7LYriF42yVpx0Na3_2IJSl5CA7/view?usp=drivesdk

Sampai ketemu di Zoom hari ini! 🤗🧩
#AlhusnaKangenKamu"""

        # 1. BUKA LINK SESUAI NOMOR
        driver.get(f"https://web.whatsapp.com/send?phone={nomor}")
        
        # Tunggu Kotak Ketik Chat Utama Muncul
        chat_box_xpath = '//div[@contenteditable="true"][@data-tab="10"] | //div[@title="Type a message"] | //div[@title="Ketik pesan"]'
        chat_box = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, chat_box_xpath))
        )
        time.sleep(2)
        
        # ==================== FASE 1: KIRIM SEMUA GAMBAR ====================
        for i, gambar_path in enumerate(list_gambar):
            print(f"   -> Mengirim Foto {i+1}/{len(list_gambar)}...")
            
            copy_image_to_clipboard(gambar_path)
            
            # Fokus ke kotak chat utama setiap kali mau paste
            chat_box = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, chat_box_xpath))
            )
            chat_box.click()
            time.sleep(0.5)
            
            # Paste Gambar
            driver.switch_to.active_element.send_keys(Keys.CONTROL, 'v') 
            time.sleep(2.5) # Tunggu layar preview terbuka
            
            # Kirim Foto (via ENTER)
            driver.switch_to.active_element.send_keys(Keys.ENTER)
            time.sleep(3) # Jeda agar kembali ke chat utama
            
        # ==================== FASE 2: KIRIM TEKS ====================
        print("   -> Menyiapkan pengiriman teks...")
        pyperclip.copy(pesan) # Copy teks dinamis yang sudah dimasukkan nama
        
        # Fokus kembali ke kotak chat utama
        chat_box = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, chat_box_xpath))
        )
        chat_box.click()
        time.sleep(0.5)
        
        # Paste Teks
        driver.switch_to.active_element.send_keys(Keys.CONTROL, 'v')
        time.sleep(2)
        
        # Kirim Teks
        driver.switch_to.active_element.send_keys(Keys.ENTER)
        
        print(f"-> ✅ Pesan & {len(list_gambar)} Foto SUKSES terkirim ke {namaPenerima} ({nomor})!")
        time.sleep(5) 
        
    except Exception as e:
        print(f"-> ❌ Gagal memproses {namaPenerima} ({nomor}).")
        print(f"   Detail Error: {type(e).__name__} - {str(e)[:100]}")

print("\nSelesai! Semua kontak dari file Excel telah diproses.")
driver.quit()