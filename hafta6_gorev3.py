# Öğrenci Adı Soyadı: Mehmet Akif Yaldız
# Öğrenci Numarası: 20253005003
# Ders: Python ile Programlama - Hafta 6 Laboratuvarı
# Tarih: 1 Kasım 2026
# Açıklama: Görev 3 - T.C. kimlik numarası doğrulama


# 1. GİRDİ 

tc_no = input("T.C. kimlik no: ")

# 2. DOĞRULA 

# Koşullar: 11 karakter, hepsi rakam (isdigit), ilk hane '0' değil
gecerli_bicim = len(tc_no) == 11 and tc_no.isdigit() and tc_no[0] != "0"

if not gecerli_bicim:
    print(f"T.C. kimlik no: {tc_no}  ->  GEÇERSİZ")
else:
    
    # 3. İŞLE
    T = 0  # Tek basamaklar (1., 3., 5., 7., 9. haneler -> indeksler 0, 2, 4, 6, 8)
    C = 0  # Çift basamaklar (2., 4., 6., 8. haneler -> indeksler 1, 3, 5, 7)

    # İlk 9 haneyi tek bir for döngüsü ile topla
    for i in range(9):
        rakam = int(tc_no[i])
        # 1., 3., 5., 7., 9. haneler (0, 2, 4, 6, 8. indeksler)
        if i % 2 == 0:
            T += rakam
        # 2., 4., 6., 8. haneler (1, 3, 5, 7. indeksler)
        else:
            C += rakam

    # Formüllere göre 10. ve 11. hane hesaplamaları
    h10 = (7 * T - C) % 10
    h11 = (T + C + h10) % 10

    # Gerçek 10. ve 11. hanelerle kıyaslama
    gercek_h10 = int(tc_no[9])
    gercek_h11 = int(tc_no[10])

    if h10 == gercek_h10 and h11 == gercek_h11:
        durum = "GEÇERLİ"
    else:
        durum = "GEÇERSİZ"

    # 4. ÇIKTI 
    print(f"Tek: {T}  Çift: {C}  10. hane: {h10}  11. hane: {h11}  ->  {durum}")