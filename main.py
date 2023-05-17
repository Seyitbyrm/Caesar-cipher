import os
from add import art, alfabe

def clear():
    os.system('clear')


def sezar():
    while True:
        print(art)
        islem = input(
            "Şifrelemek için 'encode', çözmek için 'decode' yaz:\n").lower()
        if islem == "encode" or islem == "decode":
            mesaj = input("Mesajı Giriniz:\n").lower()
            kaydirma = int(input("Kaydırma numarasını giriniz:\n"))
            kaydirma = kaydirma % 29
            yeni_mesaj = ""

            for harf in mesaj:
                if harf not in alfabe:
                    yeni_mesaj += harf
                    continue
                pozisyon = alfabe.index(harf) % 29

                if islem == "encode":
                    yeni_pozisyon = pozisyon + kaydirma
                else:
                    yeni_pozisyon = pozisyon - kaydirma

                yeni_harf = alfabe[yeni_pozisyon]
                yeni_mesaj += yeni_harf

            print(f"{islem} mesaj = {yeni_mesaj}")
        else:
            print("Geçersiz giriş")
        tekrar = input("Devam etmek istiyor musunuz (e/h)? :\n").lower()
        if tekrar != "e":
            break
        clear()


sezar()
