BATAS_LULUS = 60

def hitung_rata_rata(nilai: list[float]) -> float:
    """Mengembalikan rata-rata dari list nilai.
    Jika list kosong, mengembalikan 0.0.
    """
    if not nilai:
        return 0.0
    return sum(nilai) / len(nilai)

def status_lulus(nilai: list[float], batas: float = BATAS_LULUS) -> list[float]:
    """Mengembalikan daftar nilai yang memenuhi atau melebihi batas kelulusan."""
    return [x for x in nilai if x >= batas]

def ringkasan(nilai: list[float]) -> dict:
    """Mengembalikan dictionary berisi statistik ringkasan dari daftar nilai."""
    return {
        "jumlah": len(nilai),
        "rata_rata": hitung_rata_rata(nilai),
        "minimum": min(nilai) if nilai else None,
        "maksimum": max(nilai) if nilai else None,
        "lulus": len(status_lulus(nilai))
    }

# Testing sederhana dengan assertions saat file dipanggil langsung
if __name__ == "__main__":
    assert hitung_rata_rata([70, 80, 90]) == 80.0
    assert hitung_rata_rata([]) == 0.0
    assert status_lulus([50, 60, 70], 60) == [60, 70]
    print("Semua assertion pada proses.py LULUS!")