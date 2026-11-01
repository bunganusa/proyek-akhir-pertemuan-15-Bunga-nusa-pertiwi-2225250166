from src.input_data import input_nilai_manual, baca_nilai_dari_file
from src.proses import ringkasan
from src.output import tampilkan_ringkasan, simpan_ringkasan_ke_file

def main():
    print("==========================================")
    print("  APLIKASI ANALISIS NILAI SISWA (PROYEK)  ")
    print("==========================================")
    print("1. Input nilai manual via console")
    print("2. Baca nilai dari file 'data/nilai_siswa.txt'")
    
    pilihan = input("Pilih menu (1/2): ").strip()
    nilai_list = []
    
    if pilihan == "1":
        nilai_list = input_nilai_manual()
    elif pilihan == "2":
        nilai_list = baca_nilai_dari_file("data/nilai_siswa.txt")
    else:
        print("Pilihan tidak valid. Program berhenti.")
        return

    if not nilai_list:
        print("\n Data nilai kosong. Tidak ada yang dianalisis.")
        return

    # Proses analisis[cite: 5]
    hasil_analisis = ringkasan(nilai_list)
    
    # Tampilkan output[cite: 5, 6]
    tampilkan_ringkasan(hasil_analisis)
    
    # Simpan hasil[cite: 8, 10]
    simpan_opsi = input("Apakah ingin menyimpan hasil ke file? (y/n): ").strip().lower()
    if simpan_opsi == 'y':
        simpan_ringkasan_ke_file(hasil_analisis, "data/hasil_analisis.txt")

if __name__ == "__main__":
    main()