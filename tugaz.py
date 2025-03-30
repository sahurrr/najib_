# Fungsi untuk menghitung volume dan luas permukaan kubus
def hitung_kubus(sisi):
    # Volume kubus adalah sisi^3
    volume = sisi ** 3
    # Luas permukaan kubus adalah 6 * sisi^2
    luas_permukaan = 6 * (sisi ** 2)
    return volume, luas_permukaan

# Fungsi untuk menghitung volume dan luas permukaan balok
def hitung_balok(p, l, t):
    # Volume balok adalah panjang * lebar * tinggi
    volume = p * l * t
    # Luas permukaan balok dihitung dari jumlah luas setiap sisi
    luas_permukaan = 2 * (p * l + p * t + l * t)
    return volume, luas_permukaan

# Fungsi untuk menghitung volume dan luas permukaan bola
def hitung_bola(jari_jari):
    # Volume bola adalah (4/3) * π * jari_jari^3
    volume = (4 / 3) * 3.14159 * (jari_jari ** 3)
    # Luas permukaan bola adalah 4 * π * jari_jari^2
    luas_permukaan = 4 * 3.14159 * (jari_jari ** 2)
    return volume, luas_permukaan

# Fungsi untuk menghitung volume dan luas permukaan tabung
def hitung_tabung(jari_jari, tinggi):
    # Volume tabung adalah π * jari_jari^2 * tinggi
    volume = 3.14159 * (jari_jari ** 2) * tinggi
    # Luas permukaan tabung adalah kombinasi luas alas, tutup, dan selimut
    luas_permukaan = 2 * 3.14159 * jari_jari * (jari_jari + tinggi)
    return volume, luas_permukaan

# Fungsi untuk menghitung volume dan luas permukaan limas
def hitung_limas(luas_alas, tinggi):
    # Volume limas adalah (1/3) * luas alas * tinggi
    volume = (1 / 3) * luas_alas * tinggi
    # Luas permukaan limas dihitung sebagai asumsi sederhana
    luas_permukaan = luas_alas + (4 * tinggi)  # Asumsi tinggi mewakili sisi miring
    return volume, luas_permukaan

# Menu untuk memilih jenis bangun ruang
print("Pilih bangun ruang:")
print("1. Kubus")
print("2. Balok")
print("3. Bola")
print("4. Tabung")
print("5. L