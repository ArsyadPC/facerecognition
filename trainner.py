import os
import cv2
import numpy as np

# Path ke dataset yang berisi gambar wajah dan file yang berisi label
dataset_path = 'dataSet'
train_yml_path = 'dataTrain/train.yml'

# Inisialisasi detektor wajah menggunakan cascade classifier
face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Inisialisasi recognizer dengan algoritma Eigenfaces
recognizer = cv2.face.EigenFaceRecognizer_create()

def getImageAndLabels(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faceSamples = []
    Ids = []
    for imagePath in imagePaths:
        gray_image = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE)
        faces = face_detector.detectMultiScale(gray_image)
        for (x, y, w, h) in faces:
            faceSamples.append(gray_image[y:y+h, x:x+w])
            Id = int(os.path.split(imagePath)[-1].split(".")[1])
            Ids.append(Id)
    return faceSamples, Ids

# Memuat gambar wajah dan labelnya
faces, Ids = getImageAndLabels(dataset_path)

# Melatih recognizer
recognizer.train(faces, np.array(Ids))

# Menyimpan model yang telah dilatih
recognizer.save(train_yml_path)

print("Pelatihan selesai. Model disimpan di:", train_yml_path)
