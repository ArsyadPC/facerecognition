import MySQLdb

# Koneksi ke database
db = MySQLdb.connect("localhost", "root", "", "presensi")
cur = db.cursor()

def getPIN(npm):
    try:
        passKey = npm
        sql = "SELECT * FROM passkey WHERE pkey = %s"
        cur.execute(sql, (passKey,))
        result = cur.fetchall()
        for row in result:
            npm = row[3]
            nama = row[2]
            kelas = row[4]
            print("\nNama : %s \nNPM : %s \nKelas : %s" % (nama, npm, kelas))
            return npm, nama
    except UnboundLocalError as e:
        print("\nData Tidak ditemukan")
    finally:
        cur.close()

# Menggunakan fungsi getPIN
getPIN("npm_example")

# Tutup koneksi
db.close()
