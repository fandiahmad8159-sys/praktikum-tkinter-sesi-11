

import tkinter as tk
from tkinter import ttk, messagebox

PROGRAM_STUDI = [
    "Teknik Informatika",
    "Sistem Informasi",
    "Teknik Elektro",
    "Manajemen",
    "Akuntansi",
    "Desain Komunikasi Visual",
]

KEGIATAN = [
    "Seminar Teknologi",
    "Workshop Python",
    "Lomba Karya Ilmiah",
    "Bakti Sosial",
    "Turnamen Olahraga",
]


class AplikasiPendaftaran(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pendaftaran Kegiatan Mahasiswa")
        self.geometry("820x600")
        self.minsize(760, 560)

        # Variabel kontrol
        self.var_nama = tk.StringVar()
        self.var_prodi = tk.StringVar()
        self.var_gender = tk.StringVar(value="Laki-laki")
        self.var_kegiatan = {k: tk.BooleanVar() for k in KEGIATAN}

        self._buat_menu()
        self._buat_widget()
        self._pasang_event()
        self.entry_nama.focus_set()

    
    def _buat_menu(self):
        menubar = tk.Menu(self)

        menu_file = tk.Menu(menubar, tearoff=0)
        menu_file.add_command(label="Submit", accelerator="Enter", command=self.submit)
        menu_file.add_command(label="Reset", accelerator="Ctrl+R", command=self.reset)
        menu_file.add_separator()
        menu_file.add_command(label="Keluar", accelerator="Ctrl+Q", command=self.keluar)
        menubar.add_cascade(label="File", menu=menu_file)

        menu_bantuan = tk.Menu(menubar, tearoff=0)
        menu_bantuan.add_command(label="About", accelerator="F1", command=self.tampilkan_about)
        menubar.add_cascade(label="Bantuan", menu=menu_bantuan)

        self.config(menu=menubar)

    
    def _buat_widget(self):
        ttk.Label(
            self,
            text="Form Pendaftaran Kegiatan Mahasiswa",
            font=("Segoe UI", 16, "bold"),
        ).pack(pady=(12, 4))

        isi = ttk.Frame(self, padding=10)
        isi.pack(fill="both", expand=True)
        isi.columnconfigure(0, weight=1)
        isi.columnconfigure(1, weight=1)
        isi.rowconfigure(0, weight=1)

        
        form = ttk.LabelFrame(isi, text="Data Pendaftar", padding=10)
        form.grid(row=0, column=0, sticky="nsew", padx=(0, 6))
        form.columnconfigure(1, weight=1)

        # 1. Entry - nama
        ttk.Label(form, text="Nama").grid(row=0, column=0, sticky="w", pady=4)
        self.entry_nama = ttk.Entry(form, textvariable=self.var_nama)
        self.entry_nama.grid(row=0, column=1, sticky="ew", pady=4)

        
        ttk.Label(form, text="Program Studi").grid(row=1, column=0, sticky="w", pady=4)
        self.combo_prodi = ttk.Combobox(
            form, textvariable=self.var_prodi, values=PROGRAM_STUDI, state="readonly"
        )
        self.combo_prodi.grid(row=1, column=1, sticky="ew", pady=4)
        self.combo_prodi.set("-- Pilih Program Studi --")

        
        ttk.Label(form, text="Jenis Kelamin").grid(row=2, column=0, sticky="w", pady=4)
        frame_gender = ttk.Frame(form)
        frame_gender.grid(row=2, column=1, sticky="w", pady=4)
        for teks in ("Laki-laki", "Perempuan"):
            ttk.Radiobutton(
                frame_gender, text=teks, value=teks, variable=self.var_gender
            ).pack(side="left", padx=(0, 12))

        
        ttk.Label(form, text="Kegiatan").grid(row=3, column=0, sticky="nw", pady=4)
        frame_kegiatan = ttk.Frame(form)
        frame_kegiatan.grid(row=3, column=1, sticky="w", pady=4)
        for k in KEGIATAN:
            ttk.Checkbutton(
                frame_kegiatan,
                text=k,
                variable=self.var_kegiatan[k],
                command=self.perbarui_listbox,
            ).pack(anchor="w")

        
        ttk.Label(form, text="Alasan").grid(row=4, column=0, sticky="nw", pady=4)
        self.text_alasan = tk.Text(form, height=5, width=30, wrap="word")
        self.text_alasan.grid(row=4, column=1, sticky="ew", pady=4)

        
        frame_tombol = ttk.Frame(form)
        frame_tombol.grid(row=5, column=0, columnspan=2, pady=(10, 0))
        ttk.Button(frame_tombol, text="Submit", command=self.submit).pack(side="left", padx=5)
        ttk.Button(frame_tombol, text="Reset", command=self.reset).pack(side="left", padx=5)

        
        kanan = ttk.Frame(isi)
        kanan.grid(row=0, column=1, sticky="nsew", padx=(6, 0))
        kanan.columnconfigure(0, weight=1)
        kanan.rowconfigure(1, weight=1)

        
        frame_list = ttk.LabelFrame(kanan, text="Kegiatan Dipilih", padding=8)
        frame_list.grid(row=0, column=0, sticky="ew")
        self.listbox = tk.Listbox(frame_list, height=5)
        self.listbox.pack(fill="x")

        
        frame_info = ttk.LabelFrame(kanan, text="Ringkasan Pendaftaran", padding=8)
        frame_info.grid(row=1, column=0, sticky="nsew", pady=(8, 0))
        frame_info.columnconfigure(0, weight=1)
        frame_info.rowconfigure(0, weight=1)
        self.text_info = tk.Text(
            frame_info, height=10, width=34, state="disabled", wrap="word", bg="#f4f6f8"
        )
        self.text_info.grid(row=0, column=0, sticky="nsew")
        scroll = ttk.Scrollbar(frame_info, command=self.text_info.yview)
        scroll.grid(row=0, column=1, sticky="ns")
        self.text_info.config(yscrollcommand=scroll.set)

        self.var_status = tk.StringVar(value="Siap. Isi form lalu tekan Enter atau klik Submit.")
        ttk.Label(self, textvariable=self.var_status, relief="sunken", anchor="w").pack(
            fill="x", side="bottom"
        )

        self.perbarui_listbox()

    
    def _pasang_event(self):
        # Enter pada Entry/Combobox/jendela menjalankan Submit.
        # Pada widget Text, Enter tetap berfungsi sebagai baris baru.
        self.entry_nama.bind("<Return>", self.submit)
        self.combo_prodi.bind("<Return>", self.submit)
        self.bind("<KP_Enter>", self.submit)
        self.bind("<Control-r>", lambda e: self.reset())
        self.bind("<Control-q>", lambda e: self.keluar())
        self.bind("<F1>", lambda e: self.tampilkan_about())
        # Event mouse: ubah status bar saat kursor masuk ke kolom nama
        self.entry_nama.bind("<FocusIn>", lambda e: self.var_status.set("Isi nama lengkap Anda."))
        self.protocol("WM_DELETE_WINDOW", self.keluar)

    
    def kegiatan_terpilih(self):
        return [k for k, v in self.var_kegiatan.items() if v.get()]

    def perbarui_listbox(self):
        self.listbox.delete(0, tk.END)
        terpilih = self.kegiatan_terpilih()
        if not terpilih:
            self.listbox.insert(tk.END, "(belum ada kegiatan dipilih)")
            self.listbox.itemconfig(0, fg="gray")
            return
        for i, k in enumerate(terpilih, 1):
            self.listbox.insert(tk.END, f"{i}. {k}")

    def tulis_info(self, teks):
        self.text_info.config(state="normal")
        self.text_info.delete("1.0", tk.END)
        self.text_info.insert(tk.END, teks)
        self.text_info.config(state="disabled")

    def submit(self, event=None):
        nama = self.var_nama.get().strip()
        prodi = self.var_prodi.get()
        gender = self.var_gender.get()
        kegiatan = self.kegiatan_terpilih()
        alasan = self.text_alasan.get("1.0", tk.END).strip()

        # Validasi
        if not nama:
            messagebox.showwarning("Validasi", "Nama tidak boleh kosong!")
            self.entry_nama.focus_set()
            return
        if prodi not in PROGRAM_STUDI:
            messagebox.showwarning("Validasi", "Silakan pilih program studi.")
            self.combo_prodi.focus_set()
            return
        if not kegiatan:
            messagebox.showwarning("Validasi", "Pilih minimal satu kegiatan.")
            return

        ringkasan = (
            "PENDAFTARAN BERHASIL\n"
            "--------------------------------\n"
            f"Nama           : {nama}\n"
            f"Program Studi  : {prodi}\n"
            f"Jenis Kelamin  : {gender}\n"
            f"Kegiatan       :\n"
            + "\n".join(f"   - {k}" for k in kegiatan)
            + f"\nAlasan         : {alasan if alasan else '-'}\n"
        )
        self.tulis_info(ringkasan)
        self.var_status.set(f"Pendaftaran atas nama {nama} berhasil disimpan.")
        messagebox.showinfo("Sukses", f"Terima kasih, {nama}!\nPendaftaran Anda berhasil.")

    def reset(self):
        self.var_nama.set("")
        self.combo_prodi.set("-- Pilih Program Studi --")
        self.var_prodi.set("")
        self.var_gender.set("Laki-laki")
        for v in self.var_kegiatan.values():
            v.set(False)
        self.text_alasan.delete("1.0", tk.END)
        self.tulis_info("")
        self.perbarui_listbox()
        self.var_status.set("Form telah direset.")
        self.entry_nama.focus_set()

    def tampilkan_about(self):
        about = tk.Toplevel(self)
        about.title("About")
        about.geometry("340x200")
        about.resizable(False, False)
        about.transient(self)
        about.grab_set()

        frame = ttk.Frame(about, padding=15)
        frame.pack(fill="both", expand=True)
        ttk.Label(frame, text="Pendaftaran Kegiatan Mahasiswa",
                  font=("Segoe UI", 12, "bold")).pack(pady=(0, 6))
        ttk.Label(frame, text="Praktikum Tkinter Sesi 11\nAdvanced Widgets dan Event Handling",
                  justify="center").pack()
        ttk.Label(frame, text="Versi 1.0", foreground="gray").pack(pady=6)
        ttk.Button(frame, text="Tutup", command=about.destroy).pack(pady=(6, 0))
        about.bind("<Escape>", lambda e: about.destroy())

    def keluar(self):
        if messagebox.askyesno("Konfirmasi", "Yakin ingin keluar dari aplikasi?"):
            self.destroy()


if __name__ == "__main__":
    AplikasiPendaftaran().mainloop()