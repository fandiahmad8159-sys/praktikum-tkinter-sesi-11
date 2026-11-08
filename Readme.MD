# 🎓 Praktikum Tkinter Sesi 11 - Pendaftaran Kegiatan Mahasiswa

## 🎯 Tujuan
Membangun aplikasi GUI menggunakan Python Tkinter dengan memanfaatkan berbagai widget,
event handling, validasi input, menu, dan dialog (Advanced Widgets dan Event Handling).

## ✨ Fitur
- **Entry** untuk nama, **Combobox** untuk program studi, **Radiobutton** untuk jenis kelamin.
- **Checkbutton** untuk memilih kegiatan, **Text** untuk alasan mengikuti kegiatan.
- **Listbox** yang menampilkan kegiatan yang dipilih secara langsung.
- Tombol **Submit** dan **Reset**; ringkasan pendaftaran tampil di area informasi.
- **Validasi**: nama tidak boleh kosong, program studi harus dipilih, minimal satu kegiatan.
- **Messagebox** untuk notifikasi (peringatan validasi, sukses, konfirmasi keluar).
- **Menu File** (Submit, Reset, Keluar) dan **menu Bantuan** (About) yang membuka jendela **Toplevel**.
- **Event keyboard**: `Enter` = Submit, `Ctrl+R` = Reset, `Ctrl+Q` = Keluar, `F1` = About.
- Tata letak menggunakan **Frame/LabelFrame** dengan geometry manager `grid` dan `pack`.

## 🚀 Cara Menjalankan
1. Pastikan Python 3 terpasang (Tkinter sudah termasuk; di Linux: `sudo apt install python3-tk`).
2. Jalankan:
   ```
   python main.py
   ```

## 📁 Struktur Repository
```
praktikum-tkinter-sesi-11/
├── main.py
├── README.md
└── screenshots/
    ├── form-pendaftaran.png
    ├── pilihan-widget.png
    └── hasil-submit.png
```

## 📸 Screenshot
| Form awal | Pilihan widget terisi | Hasil submit |
|---|---|---|
| ![form](screenshots/form-pendaftaran.png) | ![widget](screenshots/pilihan-widget.png) | ![hasil](screenshots/hasil-submit.png) |

## 👤 Identitas
Nama: Fandi Ahmad   NIM: 2595114028 Kelas: Teknik Informatika (B)