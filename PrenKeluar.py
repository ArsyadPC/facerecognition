def Keluar(self):
    try:
        curs = db.cursor()  # Mendapatkan kursor dari objek database

        if self.id.get() == "None":
            messagebox.showerror("Error", "NPM harus diisi")
            return
        elif len(self.id.get()) == 0:
            messagebox.showerror("Error", "NPM Harus diisi")
            return

        day = now.strftime("%w")
        hari = satuMinggu(day)
        npm = self.id.get()
        (npmPin, namaPin) = cekPin.getPIN(npm)

        curs.execute(
            "SELECT * FROM laporan WHERE jamKeluar IS NULL AND jamMasuk IS NOT NULL AND Hari = %s ORDER BY no DESC LIMIT 1",
            (hari,))
        status = 0

        for row in curs:
            status = 1
            if status == 1:
                messagebox.showinfo("Info", "Tekan OK, Lalu Tunggu Kamera Menyala...")
                time.sleep(3)
                (npmFace, namaFace) = faceRec.getFace_info()

                if (namaPin == namaFace and npmPin == npmFace):
                    curs.execute(
                        "UPDATE laporan SET jamKeluar = CURTIME() WHERE jamKeluar IS NULL AND jamMasuk IS NOT NULL AND hari = %s ORDER BY no DESC LIMIT 1",
                        (hari,))
                    db.commit()
                    messagebox.showinfo("Info", "Proses selesai")
                else:
                    messagebox.showinfo("ERROR", "Anda Belum Masuk")

                # Menampilkan data laporan
                sql = "SELECT nama, tanggal, hari, jamMasuk, jamKeluar FROM laporan"
                curs.execute(sql)
                result = curs.fetchall()

                for row in result:
                    name = row[0]
                    tgl = str(row[1])
                    hari = str(row[2])
                    masuk = str(row[3])
                    keluar = str(row[4])

                    tk.Label(self, text=name, fg="#263942", font='Helvetica 7 bold').grid(row=4, column=1, pady=5,
                                                                                          padx=3)
                    tk.Label(self, text=tgl, fg="#263942", font='Helvetica 7 bold').grid(row=5, column=1, pady=5,
                                                                                         padx=3)
                    tk.Label(self, text=hari, fg="#263942", font='Helvetica 7 bold').grid(row=6, column=1, pady=5,
                                                                                          padx=3)
                    tk.Label(self, text=masuk, fg="#263942", font='Helvetica 7 bold').grid(row=7, column=1, pady=5,
                                                                                           padx=3)
                    tk.Label(self, text=keluar, fg="#263942", font='Helvetica 7 bold').grid(row=8, column=1, pady=5,
                                                                                            padx=3)
            break

    except TypeError:
        messagebox.showerror("ERROR", "Data Tidak ditemukan \n Silahkan Daftarkan Data Anda")
    self.controller.show_frame("PageOne")