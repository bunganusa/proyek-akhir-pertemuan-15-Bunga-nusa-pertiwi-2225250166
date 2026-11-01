from src.proses import hitung_rata_rata, status_lulus, ringkasan, BATAS_LULUS

def test_rata_rata():
    assert hitung_rata_rata([70, 80, 90]) == 80.0

def test_nilai_kosong():
    assert hitung_rata_rata([]) == 0.0

def test_status_lulus():
    assert status_lulus([60], BATAS_LULUS) == [60]

def test_ringkasan():
    hasil = ringkasan([70, 80, 90])
    assert hasil["jumlah"] == 3

if __name__ == "__main__":
    test_rata_rata()
    test_nilai_kosong()
    test_status_lulus()
    test_ringkasan()
    print("Semua pengujian berhasil!")