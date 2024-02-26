import cv2

def iou(self):
    global cam
    try:
        if self.npm.get() == "":
            messagebox.showerror("Error", "NPM harus diisi")
            return
        elif len(self.npm.get()) == 0:
            messagebox.showerror("Error", "NPM Harus diisi")
            return
        elif self.name.get() == "":
            messagebox.showerror("Error", "Nama harus diisi")
            return
        elif len(self.name.get()) == 0:
            messagebox.showerror("Error", "Nama Harus diisi")
            return
        elif self.kelas.get() == "":
            messagebox.showerror("Error", "Kelas harus diisi")
            return
        elif len(self.kelas.get()) == 0:
            messagebox.showerror("Error", "Kelas Harus diisi")
            return

        id = self.npm.get()
        nama = self.name.get()
        kelas = self.kelas.get()

        messagebox.showinfo("Info", "Tekan OK, Lalu Tunggu Kamera Menyala\nUntuk mengambil Data Wajah...")

        IoU.face_insertOrUpdate(id, nama, kelas)
        IoU.PIN_insertOrUpdate(nama, id, kelas)

        sampleNum = 0
        cam = cv2.VideoCapture(0)
        time.sleep(5)

        while True:
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:
                sampleNum += 1
                cv2.imwrite(f"dataSet/user.{id}.{sampleNum}.jpg", gray[y:y + h, x:x + w])
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.imshow('img', img)
                cv2.waitKey(50)

                if sampleNum > 50:
                    os.system("del dataTrain\\train.yml /s /q")
                    os.system("python3 Training.py")
                    os.mkdir(f"absensi\\{id}")
                    break

            cam.release()
            cv2.destroyAllWindows()

    except FileExistsError:
        messagebox.showinfo("Info", "Npm anda sudah terdaftar\ndata anda akan diupdate")
        cam.release()
        cv2.destroyAllWindows()
        self.controller.show_frame("StartPage")
