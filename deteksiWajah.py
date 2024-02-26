import cv2
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('dataTrain/train.yml')
now = datetime.datetime.now()



def getProfile(id):
    db = MySQLdb.connect("localhost", "root", "", "presensi")
    curs = db.cursor()
    cmd = "SELECT * FROM facebase WHERE npm = %s"
    curs.execute(cmd, (id,))
    profile = curs.fetchone()
    curs.close()
    return profile


def getFace_info():
    cam = cv2.VideoCapture(0)
    while True:
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)

        for (x, y, w, h) in faces:
            id, conf = recognizer.predict(gray[y:y + h, x:x + w])
            profile = getProfile(id)
            print(str(id) + " " + str(conf))

            if conf < 43:
                if profile is not None:
                    cv2.imwrite("absensi/" + profile[1] + "/" + now.strftime("%Y-%m-%d %H-%M") + "[1]" + ".jpg", img)
                    cv2.imwrite("absensi/" + profile[2] + "/" + now.strftime("%Y-%m-%d %H-%M") + "[2]" + ".jpg", img)
                    time.sleep(3)
                    return profile[1], profile[2]

        cv2.imshow('img', img)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()
