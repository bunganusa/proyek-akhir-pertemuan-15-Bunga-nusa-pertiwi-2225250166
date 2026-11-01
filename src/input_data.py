def input_nilai_manual() -> list[float]:
    """Menerima masukan nilai dari pengguna via console dengan validasi input."""
    daftar_nilai = []
    print("=== Input Data Nilai Siswa ===")
    print("Masukkan nilai satu per satu. Ketik 'selesai' atau 's' untuk mengakhiri.\n")
    
    while True:
        raw_input = input("Masukkan nilai: ").strip()
        if raw_input.lower() in ['selesai', 's']:
            break
        try:
            val = float(raw_input)
            if 0 <= val <= 100:
                daftar_nilai.append(val)
            else:
                print(" Error: Nilai harus berada dalam rentang 0 - 100.")
        except ValueError:
            print(" Error: Input tidak valid! Harap masukkan angka yang benar.")
            
    return daftar_nilai

def baca_nilai_dari_file(filepath: str) -> list[float]:
    """Membaca data nilai dari file teks[cite: 5, 6]."""
    daftar_nilai = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for baris in f:
                baris = baris.strip()
                if baris:
                    try:
                        val = float(baris)
                        daftar_nilai.append(val)
                    except ValueError:
                        continue
    except FileNotFoundError:
        print(f" Error: File {filepath} tidak ditemukan.")
    return daftar_nilai