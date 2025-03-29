def hitung_kubus(sisi):
    volume = sisi ** 3
    luas_permukaan = 6 * (sisi ** 2)
    return volume, luas_permukaan

def hitung_balok(p, l, t):
    volume = p * l * t
    luas_permukaan = 2 * (p * l + p * t + l * t)
    return volume, luas_permukaan

def hitung_bola(jari_jari):
    volume = (4 / 3) * 3.14159 * (jari_jari ** 3)
    luas_permukaan = 4 * 3.14159 * (jari_jari ** 2)
    return volume, luas_permukaan

def hitung_tabung(jari_jari, tinggi):
    volume = 3.14159 * (jari_jari ** 2) * tinggi
    luas_permukaan = 2 * 3.14159 * jari_jari * (jari_jari + tinggi)
    return volume, luas_permukaan

def hitung_limas(luas_alas, tinggi):
    volume = (1 / 3) * luas_alas * tinggi
    # Asumsi ini adalah limas segi empat
    luas_permukaan = luas_alas + (4 * tinggi)
    return volume, luas_permukaan

print("Pilih bangun ruang:")
print("1. Kubus")
print("2. Balok")
print("3. Bola")
print("4. Tabung")
print("5. Limas")

pilihan = int(input("Masukkan pilihan (1-5): "))

if pilihan == 1:
    sisi = float(input("Masukkan panjang sisi: "))
    volume, luas_permukaan = hitung_kubus(sisi)
elif pilihan == 2:
    p = float(input("Masukkan panjang: "))
    l = float(input("Masukkan lebar: "))
    t = float(input("Masukkan tinggi: "))
    volume, luas_permukaan = hitung_balok(p, l, t)
elif pilihan == 3:
    jari_jari = float(input("Masukkan jari-jari: "))
    volume, luas_permukaan = hitung_bola(jari_jari)
elif pilihan == 4:
    jari_jari = float(input("Masukkan jari-jari: "))
    tinggi = float(input("Masukkan tinggi: "))
    volume, luas_permukaan = hitung_tabung(jari_jari, tinggi)
elif pilihan == 5:
    luas_alas = float(input("Masukkan luas alas: "))
    tinggi = float(input("Masukkan tinggi: "))
    volume, luas_permukaan = hitung_limas(luas_alas, tinggi)
else:
    print("Pilihan tidak valid!")
    exit()

print(f"\nHasil Perhitungan:")
print(f"Volume: {volume:.2f}")
print(f"Luas Permukaan: {luas_permukaan:.2f}")