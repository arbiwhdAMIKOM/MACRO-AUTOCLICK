# ##INSTALASI (macOS)##
1. download Python 3.12 dari python.org - disarankan jangan menggunakan homebrew karena akan memakan waktu lama.
2. buka terminal dan ketik ini: pip3.12 install pyautogui py2app
3. lalu build dengan ketik lalu enter ini: python3.12 setup.py py2app
4. cari File .app hasil build biasanya ada di folder dist/AutoPresser.app. Double-click langsung bisa jalan.

# Izin yang Diperlukan di macOS
Karena AutoPresser mengontrol keyboard dan mouse, macOS memerlukan izin khusus.
# Accessibility (wajib)
Diperlukan agar aplikasi bisa mensimulasikan penekanan tombol dan klik mouse.
1. Buka System Preferences → Security & Privacy → tab Privacy
2. Pilih Accessibility di panel kiri
3. Klik ikon gembok di bawah dan masukkan password
4. Klik tombol + dan tambahkan AutoPresser (dari folder dist/)
5. Centang AutoPresser di daftar

Jika masih belum bisa run maka lakukan ini:
1. Buka System Preferences → Security & Privacy → tab Privacy
2. Pilih Screen Recording di panel kiri
3. Tambahkan dan centang AutoPresser seperti langkah di atas
Catatan: Setelah memberikan izin, restart AutoPresser agar izin aktif.
4. Jika menggunakan macOS 13 (Ventura) ke atas, pengaturan ada di System Settings → Privacy & Security.

# INSTALASI (Windows)##
Requirement:
Python 3.x dari python.org

Lalu buka cmd; Windows + R "cmd" dan pip install:
1. pip install pyautogui pyinstaller pynput
Build:
2. pyinstaller build_windows.spec.py

biasanya File .exe hasil build ada di folder dist/.

# MACRO-AUTOCLICK
Aplikasi ringan berbasis Python/Tkinter untuk otomatisasi penekanan tombol keyboard (macro) dan klik mouse otomatis (auto clicker). Tersedia untuk **macOS** dan **Windows**.
## Fitur
- Mode **Keyboard Macro**: tekan tombol tertentu secara berkala dengan jeda (delay) dan repetisi yang bisa diatur
- Mode **Auto Clicker**: klik mouse otomatis dengan interval yang bisa diatur
- Countdown 5 detik sebelum mulai (memberi waktu pindah ke aplikasi target)
- Hotkey `[` untuk START dan `]` untuk STOP
- Window selalu tampil di atas aplikasi lain agar tombol STOP mudah dijangkau
- Safety check: interval auto clicker minimal 0.01 detik

## Hotkey
| Tombol | Fungsi |
|--------|--------|
| `[`    | START  |
| `]`    | STOP   |
-------------------
Tombol `[` dan `]` berada di sebelah kanan huruf **P** pada keyboard.
> **macOS:** Hotkey hanya aktif saat jendela AutoPresser sedang fokus. Klik dulu jendela AutoPresser sebelum menekan `[` atau `]`.  
> **Windows:** Hotkey aktif secara global, bisa dipakai bahkan saat jendela lain aktif.

## Cara Pakai
1. Buka aplikasi **AutoPresser**
2. Pilih mode: **Keyboard Macro** atau **Auto Clicker**
3. Atur parameter sesuai kebutuhan
4. Klik tombol **START** atau tekan `[`
5. Pindah ke aplikasi yang ingin diotomatisasi (ada countdown 5 detik)
6. Untuk berhenti: klik tombol **STOP** atau tekan `]`
