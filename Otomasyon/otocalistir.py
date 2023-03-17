import time
from otomasyon import *

print("""========================
    Yapacağiniz İşlem Numarası Seçiniz
    1) Öğrenci Ekle
    2) Öğreci Ara
    3) Tüm Öğrencileri Görüntüle
    4) Öğrenci Kaydını Sil
    Sistemden Çıkış Yapmak İçin 'q' tıklayınız!
=============================""")
Otomasyon = Otomasyon()

while True:
    islem = input('Yapmak istediğiniz işlem numarsını giriniz:')

    if islem == '1':
        isim = input('Öğrenci Adı:')
        soyad = input('Öğrenci Soyadı:')
        bolum = input("Bölümü:")
        kayit_yili = int(input('Kayıt Yılı:'))
        ogre_no = int(input('Öğrenci Numarası:'))
        yeni_ogr = Ogrenci(isim,soyad,bolum,kayit_yili,ogre_no)
        print('Öğrenci Ekleniyor')
        time.sleep(2)
        Otomasyon.ogr_ekle(yeni_ogr)
        print('Öğrenci başarıyla otomasyona eklendi')
    
    if islem == '2':
        ogre_no = int(input('Öğrenci Numarasını giriniz= '))
        print('Otomasyon taranıyor!')
        time.sleep(2)
        Otomasyon.ogr_ara(ogre_no)

    if islem == '3':
        print('Öğrenciler Aranıyor')
        print("===========")
        time.sleep(2)
        Otomasyon.ogrleri_goster()

    if islem == '4':
        ogre_no = int(input("Hangi ogrenciyi silmek istiyorsunuz:"))
        print('Silme işlemi gerçekleşiyor.')
        time.sleep(2)
        Otomasyon.ogr_sil(ogre_no)
        print('Silindi!')

    if islem == 'q':
            print('Otomasyondan çıkış yapılıyor...')        
            time.sleep(2)
            print('Çıkış yapıldı!')
            break
    else:
        print('Geçersiz işlem numarası girdiniz!')
    

