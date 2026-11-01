#Öğrenci Adı Soyadı: Mehmet Akif Yaldız
# Öğrenci Numarası: 20253005003
# Ders: Python ile Programlama - Hafta 6 Laboratuvarı
# Tarih: 1 Kasım 2026
# Açıklama: Görev 1 - Üçgen Analizörü

import math
while True:
    kenar1 = float(input("a: "))
    kenar2 = float(input("b: "))
    kenar3 = float(input("c: "))

    # Kenarlar pozitif mi kontrolü
    if kenar1 <= 0 or kenar2 <= 0 or kenar3 <= 0:
        print("Uyarı: Kenar uzunlukları pozitif olmalıdır! Tekrar deneyin.\n")
        continue

    # Üçgen eşitsizliği kontrolü
    if not (kenar1 + kenar2 > kenar3 and kenar1 + kenar3 > kenar2 and kenar2 + kenar3 > kenar1):
        print("Uyarı: Üçgen eşitsizliği sağlanmıyor! Tekrar deneyin.\n")
        continue

    # Geçerli girdi alındıysa döngüyü sonlandır
    break



#  Formülde 'a en uzun kenar' kuralına göre kenarları a, b, c olarak atama (Liste kullanmadan)
if kenar1 >= kenar2 and kenar1 >= kenar3:
    a = kenar1
    b = kenar2
    c = kenar3
elif kenar2 >= kenar1 and kenar2 >= kenar3:
    a = kenar2
    b = kenar1
    c = kenar3
else:
    a = kenar3
    b = kenar1
    c = kenar2

# B) Kenarlarına göre sınıflandırma
if math.isclose(a, b) and math.isclose(b, c):
    kenar_turu = "Eşkenar"
elif math.isclose(a, b) or math.isclose(b, c) or math.isclose(a, c):
    kenar_turu = "İkizkenar"
else:
    kenar_turu = "Çeşitkenar"

#  Çevre ve Heron Formülü ile Alan Hesabı
cevre = a + b + c
u = cevre / 2
alan = math.sqrt(u * (u - a) * (u - b) * (u - c))

#  Kosinüs Teoremi ile en büyük açının bulunması (a en uzun kenar olduğu için karşısındaki açı en büyüktür)
cos_alpha = (b**2 + c**2 - a**2) / (2 * b * c)

# Sayısal yuvarlama hatalarına karşı cos değerini [-1, 1] aralığında sınırlama
if cos_alpha > 1.0:
    cos_alpha = 1.0
elif cos_alpha < -1.0:
    cos_alpha = -1.0

aci_radyan = math.acos(cos_alpha)
en_buyuk_aci = math.degrees(aci_radyan)

#  Açısına göre sınıflandırma 
if math.isclose(en_buyuk_aci, 90):
    aci_turu = "Dik açılı"
elif en_buyuk_aci < 90:
    aci_turu = "Dar açılı"
else:
    aci_turu = "Geniş açılı"


print(f"Tür: {kenar_turu}, {aci_turu}")
print(f"Çevre: {cevre:.2f}  Alan: {alan:.2f}  En büyük açı: {en_buyuk_aci:.2f}°")