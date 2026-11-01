from src.proses import hitung_rata_rata, status_lulus, ringkasan

def jalankan_uji():
    print("=== Menjalankan Pengujian Proyek (Test Cases) ===\n")

    # TC01: Rata-rata normal
    assert hitung_rata_rata([70, 80, 90]) == 80.0, "TC01 Gagal: Rata-rata normal salah"
    print("[PASS] TC01: Rata-rata kondisi normal")

    # TC02: List kosong (Empty case agar tidak ZeroDivisionError)
    assert hitung_rata_rata([]) == 0, "TC02 Gagal: Rata-rata list kosong harus 0"
    print("[PASS] TC02: Rata-rata list kosong")

    # TC03: Kelulusan tepat pada nilai batas (Boundary case)
    assert len(status_lulus([60])) == 1, "TC03 Gagal: Nilai 60 seharusnya lulus"
    print("[PASS] TC03: Kelulusan tepat pada nilai batas (60)")

    # TC04: Kelulusan nilai di bawah batas
    assert len(status_lulus([59])) == 0, "TC04 Gagal: Nilai 59 seharusnya tidak lulus"
    print("[PASS] TC04: Kelulusan nilai di bawah batas (59)")

    # TC05: Ringkasan data lengkap
    res = ringkasan([50, 60, 70])
    assert res["jumlah"] == 3, "TC05 Gagal: Jumlah data salah"
    assert res["rata_rata"] == 60.0, "TC05 Gagal: Rata-rata ringkasan salah"
    assert res["lulus"] == 2, "TC05 Gagal: Jumlah lulus ringkasan salah"
    print("[PASS] TC05: Ringkasan data lengkap")

    print("\n------------------------------------------------")
    print("Semua test case berhasil dijalankan (PASS)!")
    print("------------------------------------------------")

if __name__ == "__main__":
    jalankan_uji()