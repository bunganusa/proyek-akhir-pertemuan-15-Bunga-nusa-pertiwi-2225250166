def tampilkan_ringkasan(hasil: dict) -> None:
    """Menampilkan ringkasan hasil analisis ke layar terminal."""
    print("\n====================================")
    print("     HASIL ANALISIS NILAI SISWA     ")
    print("====================================")
    print(f"Jumlah Siswa / Nilai : {hasil['jumlah']}")
    print(f"Rata-rata Nilai      : {hasil['rata_rata']:.2f}")
    print(f"Nilai Terendah       : {hasil['minimum']}")
    print(f"Nilai Tertinggi      : {hasil['maksimum']}")
    print(f"Jumlah Siswa Lulus   : {hasil['lulus']}")
    print(f"Jumlah Tidak Lulus   : {hasil['jumlah'] - hasil['lulus']}")
    print("====================================\n")

def simpan_ringkasan_ke_file(hasil: dict, filepath: str) -> None:
    """Menyimpan hasil analisis nilai ke dalam file teks."""
    try:
        with open(filepath, 'a', encoding='utf-8') as f:  # Gunakan mode 'a' agar tidak menimpa data
            f.write("=== RINGKASAN HASIL ANALISIS ===\n")
            f.write(f"Jumlah Data : {hasil['jumlah']}\n")
            f.write(f"Rata-Rata   : {hasil['rata_rata']:.2f}\n")
            f.write(f"Minimum     : {hasil['minimum']}\n")
            f.write(f"Maksimum    : {hasil['maksimum']}\n")
            f.write(f"Siswa Lulus : {hasil['lulus']}\n\n")
        print(f" Hasil berhasil disimpan ke '{filepath}'.")
    except Exception as e:
        print(f" Gagal menyimpan file: {e}")