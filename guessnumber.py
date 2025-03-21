import random
import time

def zorluk_seviyesi():
    print("Zorluk Seçenekleri:")
    print("1 - Kolay (1 ile 50 arasında)")
    print("2 - Orta (1 ile 100 arasında)")
    print("3 - Zor (1 ile 200 arasında)")

    secim = int(input("Zorluk seviyesini seç (1/2/3): "))
    
    if secim == 1:
        return 50  # Kolay seviye: 1 ile 50 arasında
    elif secim == 2:
        return 100  # Orta seviye: 1 ile 100 arasında
    elif secim == 3:
        return 200  # Zor seviye: 1 ile 200 arasında
    else:
        print("Geçersiz seçenek. Kolay seviyeye geçiliyor.")
        return 50  # Varsayılan olarak Kolay seviye

def sayi_tahmin_oyunu():
    print("Sayı Tahmin Oyununa Hoş Geldiniz!")
    
    # Zorluk seviyesini seç
    ust_sinir = zorluk_seviyesi()
    
    # Bilgisayarın rastgele bir sayı seçmesini sağlıyoruz
    sayi = random.randint(1, ust_sinir)
    
    # Kullanıcının tahmin hakları
    tahmin_haklari = 10
    dogru_tahmin = False
    tahmin_sayisi = 0
    baslangic_zamani = time.time()  # Oyun süresi başlatılıyor
    
    print("Sayı Tahmin Oyunu - by rheme18")
    print(f"1 ile {ust_sinir} arasında bir sayı tuttum. Hadi tahmin etmeye başla!")
    
    while tahmin_haklari > 0:
        print(f"Bu kadar hakkınız kaldı: {tahmin_haklari}")
        tahmin = int(input("Tahmininizi yapın: "))
        tahmin_sayisi += 1  # Her tahminde sayıcıyı artır
        
        if tahmin < sayi:
            print("Daha büyük bir sayı söyle.")
        elif tahmin > sayi:
            print("Daha küçük bir sayı söyle.")
        else:
            print(f"Tebrikler! {tahmin} sayısını bildiniz.")
            dogru_tahmin = True
            break
        
        tahmin_haklari -= 1

    if tahmin_haklari == 0 and not dogru_tahmin:
        print(f"Maalesef, haklarınız bitti! Doğru sayı {sayi} idi.")
    
    # Oyun süresini hesapla
    bitis_zamani = time.time()
    oyun_suresi = bitis_zamani - baslangic_zamani

    # İstatistikleri göster
    print("\n--- İstatistikler ---")
    print(f"Doğru tahmin: {dogru_tahmin}")
    print(f"Tahmin sayısı: {tahmin_sayisi}")
    print(f"Oyunun tamamlanma süresi: {oyun_suresi:.2f} saniye")
    
    # Kullanıcıya başarı oranı ve skor
    if dogru_tahmin:
        print("Başarı oranınız: %100")
    else:
        print("Başarı oranınız: %0")
        
# Oyun bitince bekleme
    input("Oyun Bitti Enter'a Bas...")
    
    print("by rheme18")
    
# Oyunu başlat
sayi_tahmin_oyunu()
