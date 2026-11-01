# Öğrenci Adı Soyadı: Mehmet Akif Yaldız
# Öğrenci Numarası: 20253005003
# Ders: Python ile Programlama - Hafta 6 Laboratuvarı
# Tarih: 1 Kasım 2026
# Açıklama: Görev 5 - Adam asmaca
gizli_kelime = "KOŞUL"
tahminler = ""  
hata_sayisi = 0
maks_hata = 6


while hata_sayisi < maks_hata:
    
    # A) DURUM ÇIKTISI (Mevcut kelime durumu ve hata sayısı)
    
    gorunum = ""
    tamamlandi = True

    for harf in gizli_kelime:
        if harf in tahminler:
            gorunum += harf + " "
        else:
            gorunum += "_ "
            tamamlandi = False

    gorunum = gorunum.rstrip()  # Sondaki gereksiz boşluğu temizle
    print(f"{gorunum}   (hata: {hata_sayisi}/{maks_hata})")

    # Kelime tamamen bilindiyse döngüden çık
    if tamamlandi:
        print("Kazandınız!")
        break

    # 1. GİRDİ
    giris = input("Harf: ")

    # 2. DOĞRULA (Tek harf ve daha önce denenme kontrolü)
    # Tek harf kontrolü
    if len(giris) != 1 or not giris.isalpha():
        print("-> Lütfen yalnızca tek bir harf girin.")
        continue

    # Türkçe 'i' / 'İ' dönüşüm ipucu kontrolü
    if giris == "i":
        harf = "İ"
    elif giris == "ı":
        harf = "I"
    else:
        harf = giris.upper()

    # Daha önce denenmiş harf kontrolü
    if harf in tahminler:
        print("-> Bu harfi zaten denediniz.")
        continue

    # 3. İŞLE
    tahminler += harf  # Denenen harfi diziye ekle

    # Yanlış tahmin kontrolü
    if harf not in gizli_kelime:
        hata_sayisi += 1

else:
    # 6 hata hakkı dolup döngü normal bittiğinde çalışır (while ... else)
    print(f"\nKaybettiniz! (hata: {hata_sayisi}/{maks_hata})")
    print(f"Gizli kelime: {gizli_kelime}")