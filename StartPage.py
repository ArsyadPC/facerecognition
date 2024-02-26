import tkinter as tk
from tkinter import font as tkfont

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        render = PhotoImage(file='homepagepic.png')
        img = tk.Label(self, image=render)
        img.image = render
        img.grid(row=0, column=1, rowspan=4, sticky="nsew")
        label = tk.Label(self, text="Selamat Datang", font=controller.title_font, fg="#263942")
        label.grid(row=0, sticky="ew")
        button1 = tk.Button(self, text=" Kehadiran ", fg="#ffffff", bg="#263942",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text=" Daftar & Update data ", fg="#ffffff", bg="#263942",
                            command=lambda: controller.show_frame("PageTwo"))
        button3 = tk.Button(self, text="Exit", fg="#263942", bg="#ffffff", command=self.on_closing)
        button1.grid(row=1, column=0, ipady=3, ipadx=7)
        button2.grid(row=2, column=0, ipady=3, ipadx=2)
        button3.grid(row=3, column=0, ipady=3, ipadx=32)

    def on_closing(self):
        self.controller.destroy()
