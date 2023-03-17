import sqlite3


class Ogrenci():
    def __init__(self, isim, soyisim, bolum, kayit_yili, ogr_no):
        self.isim = isim
        self.soyisim = soyisim
        self.bolum = bolum
        self.kayit_yili = kayit_yili
        self.ogr_no = ogr_no
    def __str__(self):
        return "Ad {}\nSoyad {}\Bölüm {}\nKayıt Yılı {}\nÖğrenci Numarası {}\n".format(self.isim,self.soyisim, self.bolum, self.kayit_yili, self.ogr_no)

class Otomasyon():
    def __init__(self):
        self.baglanti()
    
    def baglanti(self):
        self.baglan = sqlite3.connect("otomasyon.db")
        self.cursor = self.baglan.cursor()
        
        sorgu = "CREATE TABLE IF NOT EXISTS otomasyon (isim TEXT, soyisim TEXT, bolum TEXT, kayit_yili INT, ogr_no TEXT)"
        self.cursor.execute(sorgu)
        self.baglan.commit()


    def ogr_ekle(self,ogr):
        sorgu = "INSERT INTO otomasyon VALUES (?,?,?,?,?)"
        self.cursor.execute(sorgu,(ogr.isim,ogr.soyisim,ogr.bolum,ogr.kayit_yili,ogr.ogr_no))
        self.baglan.commit()

    def ogrleri_goster(self):
        sorgu = "SELECT * FROM otomasyon"
        self.cursor.execute(sorgu)
        ogrenciler = self.cursor.fetchall()

        if len(ogrenciler) == 0:
            print('Otomasyonda Öğrenci Bulunmamaktadır')

        else:
            for i in ogrenciler:
                ogrenci =  Ogrenci(i[0],i[1],i[2],i[3],i[4])
                print(ogrenci)
    
    def ogr_ara(self,ogr_no):
        sorgu = "SELECT * FROM otomasyon WHERE ogr_no=?"
        self.cursor.execute(sorgu,(ogr_no,))
        ogrenci = self.cursor.fetchall()

        if len(ogrenci)==0:
            print("Böyle bir öğrenci yoktur")
        else:
            ogrno = Ogrenci(ogrenci[0][0],ogrenci[0][1],ogrenci[0][2],ogrenci[0][3],ogrenci[0][4])
            print(ogrno)

    def ogr_sil(self,ogr_no):
        sorgu = "delete from otomasyon where ogr_no=?"
        self.baglan.execute(sorgu,(ogr_no,))
        self.baglan.commit()

        


