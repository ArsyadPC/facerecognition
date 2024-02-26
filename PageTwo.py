import tkinter as tk
from tkinter import font as tkfont

class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        tk.Label(self, text="Masukan NPM", fg="#263942", font='Helvetica 10 bold').grid(row=0, column=0, pady=10, padx=5)
        self.npm = tk.Entry(self, borderwidth=3, bg="lightgrey", font='Helvetica 11')
        self.npm.grid(row=0, column=1, pady=10, padx=10)

        tk.Label(self, text="Masukan Nama", fg="#263942", font='Helvetica 10 bold').grid(row=1, column=0, pady=10, padx=5)
        self.name = tk.Entry(self, borderwidth=3, bg="lightgrey", font='Helvetica 11')
        self.name.grid(row=1, column=1, pady=10, padx=10)

        tk.Label(self, text="Masukan Kelas", fg="#263942", font='Helvetica 10 bold').grid(row=2, column=0, pady=10, padx=5)
        self.kelas = tk.Entry(self, borderwidth=3, bg="lightgrey", font='Helvetica 11')
        self.kelas.grid(row=2, column=1, pady=10, padx=10)

        self.buttoncanc = tk.Button(self, text="Kembali", bg="#ffffff", fg="#263942", command=lambda: controller.show_frame("StartPage"))
        self.buttoncanc.grid(row=4, column=2, pady=7, ipadx=5, ipady=4)

        self.buttoIn = tk.Button(self, text="Daftar", fg="#ffffff", bg="#263942", command=self.iou)
        self.buttoIn.grid(row=4, column=1, pady=7, ipadx=5, ipady=4)

    def iou(self):
        try:
            if self.npm.get() == "None":
                messagebox.showerror("Error", "NPM harus diisi")
                return
            elif len(self.npm.get()) == 0:
                messagebox.showerror("Error", "NPM Harus diisi")
                return
            elif self.name.get() == "None":
                messagebox.showerror("Error", "Nama harus diisi")
                return
            elif len(self.name.get()) == 0:
                messagebox.showerror("Error", "Nama Harus diisi")
                return
            elif self.kelas.get() == "None":
                messagebox.showerror("Error", "Kelas harus diisi")
                return
            elif len(self.kelas.get()) == 0:
                messagebox.showerror("Error", "Kelas Harus diisi")
                return

            id = self.npm.get()
            nama = self.name.get()
            kelas = self.kelas.get()

            # Panggil fungsi untuk memproses data
            # IoU.face_insertOrUpdate(id, nama, kelas)
            # IoU.PIN_insertOrUpdate(nama, id, kelas)

            messagebox.showinfo("Info", "Data berhasil didaftarkan!")

            # Reset nilai entry setelah berhasil
            self.npm.delete(0, 'end')
            self.name.delete(0, 'end')
            self.kelas.delete(0, 'end')
        except Exception as e:
            messagebox.showerror("Error", str(e))
