import random

def sayi_tahmin_oyunu():
    print("Sayı Tahmin Oyununa Hoş Geldiniz!")
    print("1 ile 100 arasında bir sayı seçildi. Tahmin edin!")

    hedef_sayi = random.randint(1, 100)
    tahmin_sayisi = 0

    while True:
        tahmin = int(input("Tahmininiz: "))

        tahmin_sayisi += 1

        if tahmin < hedef_sayi:
            print("Daha yüksek bir sayı girin.")
        elif tahmin > hedef_sayi:
            print("Daha düşük bir sayı girin.")
        else:
            print(f"Tebrikler! {hedef_sayi} sayısını {tahmin_sayisi} tahminde buldunuz.")
            break

if __name__ == "__main__":
    sayi_tahmin_oyunu()
