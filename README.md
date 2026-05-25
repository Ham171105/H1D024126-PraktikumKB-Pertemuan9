# Tugas Praktikum Kecerdasan Buatan - Pertemuan 9


* **Nama:** Mohamad Ilham Huda Saputra
* **NIM:** H1D024126
* **Shift Praktikum:** Shift A

---

## 🧬 Deskripsi Tugas & Percobaan
Pada praktikum kali ini, dilakukan implementasi **Algoritma Genetika (Genetic Algorithm)** untuk menyelesaikan studi kasus klasik **Knapsack Problem Dasar**. 

Program ini bertujuan untuk mencari kombinasi barang terbaik yang dimasukkan ke dalam tas guna memaksimalkan **Nilai Keuntungan (Value)** dengan batasan **Kapasitas Beban Maksimal (Weight)** sebesar **50**.

### 🛠️ Alur Algoritma Genetika yang Diterapkan:
1. **Inisialisasi Populasi:** Membentuk individu (kromosom biner `0` dan `1`) secara acak dengan ukuran populasi sebanyak 10.
2. **Evaluasi Fitness:** Menghitung total keuntungan barang. Jika total bobot melebihi kapasitas tas (50), individu akan dikenakan pinalti nilai fitness = 0.
3. **Seleksi Orang Tua:** Menggunakan metode **Roulette Wheel Selection (RWS)**.
4. **Crossover:** Menggunakan metode **One-Point Crossover** dengan probabilitas 0.8.
5. **Mutasi:** Menggunakan metode **Flip Bit Mutation** dengan probabilitas 0.1.
6. **Evolusi:** Proses diulang terus-menerus selama 50 generasi.

---

## 💻 Spesifikasi File & Library
* **Bahasa Pemrograman:** Python
* **File Utama:** `tugas9_ga.py`
* **Library yang Digunakan:**
  * `random` (bawaan Python untuk proses stokastik Algen)
  * `matplotlib` (untuk visualisasi grafik konvergensi fitness)

---

## 📊 Hasil Output & Grafik
Ketika program `tugas9_ga.py` dijalankan, sistem akan memproses evolusi dan memunculkan jendela visualisasi grafik (`matplotlib`) yang melacak pergerakan:
* **Garis Biru:** Nilai Fitness Tertinggi di setiap generasi.
* **Garis Merah:** Rerata (Average) Fitness populasi.
* **Garis Jingga:** Nilai Fitness Terendah di setiap generasi.

*Catatan: Karena Algoritma Genetika bersifat stokastik (menggunakan nilai acak), jumlah barang yang terpilih (3 atau 4 barang) dan bentuk grafik konvergensi dapat bervariasi di setiap penekanan tombol Run/Play.*
