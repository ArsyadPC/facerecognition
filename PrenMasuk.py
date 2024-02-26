def Masuk(self):
    try:
        curs = db.cursor()  # Mendapatkan kursor dari objek database
        curs1 = db.cursor()

        if self.id.get() == "None":
            messagebox.showerror("Error", "NPM harus diisi")
            return
        elif len(self.id.get()) == 0:
            messagebox.showerror("Error", "NPM Harus diisi")
            return

        npm = self.id.get()
        (npmPin, namaPin) = cekPin.getPIN(npm)

        messagebox.showinfo("Info", "Tekan OK, Lalu Tunggu Kamera Menyala...")
        time.sleep(3)

        (npmFace, namaFace) = faceRec.getFace_info()
        messagebox.showinfo("Info", "Deteksi wajah selesai")

        day = now.strftime("%w")
        hari = satuMinggu(day)

        if (namaPin == namaFace and npmPin == npmFace):
            curs.execute("INSERT INTO laporan (npm, nama) VALUES (%s, %s)", (npmPin, namaPin))
            curs1.execute(
                "UPDATE laporan SET tanggal = CURDATE(), hari = %s, jamMasuk = CURTIME() WHERE npm = %s ORDER BY no DESC LIMIT 1",
                (hari, npmPin))
            db.commit()
        else:
            messagebox.showinfo("ERROR", "NPM dan Wajah Tidak Sesuai")

    except TypeError:
        messagebox.showerror("ERROR", "Data Tidak ditemukan \nSilahkan Daftarkan Data anda")

    self.controller.show_frame("StartPage")
