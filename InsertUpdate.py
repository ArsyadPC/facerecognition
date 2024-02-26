import cv2
import MySQLdb


detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
db = MySQLdb.connect("localhost", "root", "", "presensi")


def face_insertOrUpdate(id, nama, kelas):
    curs = db.cursor()
    curs.execute("SELECT * FROM facebase WHERE npm=%s", (str(id),))
    statData = 0
    for row in curs:
        statData = 1
        if statData == 1:
            curs.execute("UPDATE facebase SET nama=%s, kelas=%s WHERE npm=%s", (nama, kelas, str(id)))
            db.commit()
            curs.close()
        else:
            curs.execute("INSERT INTO facebase (npm, nama, kelas) VALUES (%s, %s, %s)", (id, nama, kelas))
            db.commit()
            curs.close()


def PIN_insertOrUpdate(nama, id, kelas):
    passKey = id
    attempt = 0
    max_attempt = 3

    while attempt < max_attempt:
        if passKey and len(passKey) == 8:
            curs = db.cursor()
            curs2 = db.cursor()

            curs.execute("SELECT * FROM passkey WHERE pkey=%s", [passKey])
            curs2.execute("SELECT * FROM passkey WHERE npm=%s", [id])
            curs3.execute("SELECT * FROM t_" + id)  # Anda perlu mendefinisikan curs3 sebelumnya

            statusData = 0
            for row in curs2:
                statusData = 1
                if statusData == 1:
                    curs2.execute("UPDATE passkey SET nama=%s, kelas=%s, pkey=%s WHERE npm=%s",
                                  (nama, kelas, passKey, id))
                    db.commit()
                    curs.close()
                    curs2.close()
                    curs3.close()
                else:
                    curs.execute("INSERT INTO passkey (pkey, npm, nama, kelas) VALUES (%s, %s, %s, %s)",
                                 (str(passKey), id, nama, kelas))
                    db.commit()
                    curs.close()
                break
            else:
                print("\nPIN yang dimasukkan salah")
                attempt += 1
                continue
        else:
            print("\nPIN yang dimasukkan salah")
            attempt += 1
            continue
