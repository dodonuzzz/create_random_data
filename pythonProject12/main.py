import csv
import random

def rastgele_veri_olustur():
    ad = f"Öğrenci_{random.randint(1, 100)}"
    yas = random.randint(18, 25)
    puan = round(random.uniform(0, 100), 2)  # Puanı iki ondalık basamağa yuvarla
    return [ad, yas, puan]

with open("Rastgele_veri.csv", "w", newline="") as dosya:
    yazici = csv.writer(dosya)
    yazici.writerow(["Ad", "Yaş", "Puan"])

    for i in range(100):
        veri = rastgele_veri_olustur()

        # Belirli bir olasılıkla satırı boş bırakın
        if random.random() < 0.2:
            veri[random.randint(0, 2)] = ''

        yazici.writerow(veri)

