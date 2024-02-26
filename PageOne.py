import tkinter as tk
from tkinter import font as tkfont

class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        tk.Label(self, text="Masukan NPM", fg="#263942", font='Helvetica 10 bold').grid(row=0, column=0, pady=10, padx=5)
        self.id = tk.Entry(self, borderwidth=3, bg="lightgrey", font='Helvetica 11')
        self.id.grid(row=0, column=1, pady=10, padx=10)

        self.buttoncanc = tk.Button(self, text="Cancel", bg="#ffffff", fg="#263942", command=lambda: controller.show_frame("StartPage"))
        self.buttoIn = tk.Button(self, text="Masuk", fg="#ffffff", bg="#263942", command=self.Masuk)
        self.buttoOut = tk.Button(self, text="Keluar", fg="#ffffff", bg="#263942", command=self.Keluar)

        self.buttoncanc.grid(row=1, column=2, pady=7, ipadx=5, ipady=4)
        self.buttoIn.grid(row=1, column=0, pady=7, ipadx=5, ipady=4)
        self.buttoOut.grid(row=1, column=1, pady=7, ipadx=5, ipady=4)

    def Masuk(self):
        try:
            npm = self.id.get()
            # Panggil fungsi untuk proses masuk
            # result = IoU.masuk(npm)
            # Jika berhasil
            # messagebox.showinfo("Info", result)
            # Jika gagal
            # messagebox.showerror("Error", result)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def Keluar(self):
        try:
            npm = self.id.get()
            # Panggil fungsi untuk proses keluar
            # result = IoU.keluar(npm)
            # Jika berhasil
            # messagebox.showinfo("Info", result)
            # Jika gagal
            # messagebox.showerror("Error", result)
        except Exception as e:
            messagebox.showerror("Error", str(e))
