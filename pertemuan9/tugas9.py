import random
import matplotlib.pyplot as plt

barang = [
    ['Barang1', 60, 10],
    ['Barang2', 100, 20],
    ['Barang3', 120, 30],
    ['Barang4', 80, 15],
    ['Barang5', 90, 25],
    ['Barang6', 70, 12],
    ['Barang7', 85, 18],
    ['Barang8', 95, 22]
]

kapasitas_tas = 50
ukuran_populasi = 50
probabilitas_crossover = 0.8
probabilitas_mutasi = 0.1
jumlah_generasi = 100


def inisialisasi_populasi(ukuran_populasi, jumlah_barang):
    return [[random.randint(0, 1) for _ in range(jumlah_barang)] for _ in range(ukuran_populasi)]

def hitung_fitness(individu, barang, kapasitas_tas):
    total_nilai = 0
    total_bobot = 0
    for i in range(len(individu)):
        if individu[i] == 1:
            total_nilai += barang[i][1]
            total_bobot += barang[i][2]
    if total_bobot > kapasitas_tas:
        return 0  
    return total_nilai

def seleksi_orang_tua(populasi, nilai_fitness):
    total_fitness = sum(nilai_fitness)
    if total_fitness == 0:
        return random.choice(populasi)
    probabilitas_seleksi = [f / total_fitness for f in nilai_fitness]
    return random.choices(populasi, weights=probabilitas_seleksi, k=1)[0]

def crossover(parent1, parent2, probabilitas_crossover):
    if random.random() < probabilitas_crossover:
        titik_potong = random.randint(1, len(parent1) - 1)
        child1 = parent1[:titik_potong] + parent2[titik_potong:]
        child2 = parent2[:titik_potong] + parent1[titik_potong:]
        return child1, child2
    return parent1.copy(), parent2.copy()

def mutasi(individu, probabilitas_mutasi):
    for i in range(len(individu)):
        if random.random() < probabilitas_mutasi:
            individu[i] = 1 - individu[i]
    return individu


populasi = inisialisasi_populasi(ukuran_populasi, len(barang))
history_fitness_terbaik = []
history_fitness_rata_rata = []
history_fitness_terendah = []
semua_fitness_individu = []

print("Mulai memproses Algoritma Genetika...")

for generasi in range(jumlah_generasi):
    nilai_fitness = [hitung_fitness(ind, barang, kapasitas_tas) for ind in populasi]
    
    fitness_terbaik = max(nilai_fitness)
    fitness_rata_rata = sum(nilai_fitness) / ukuran_populasi
    fitness_terendah = min(nilai_fitness)
    
    history_fitness_terbaik.append(fitness_terbaik)
    history_fitness_rata_rata.append(fitness_rata_rata)
    history_fitness_terendah.append(fitness_terendah)
    semua_fitness_individu.append(nilai_fitness.copy())
    
    populasi_baru = []
    while len(populasi_baru) < ukuran_populasi:
        p1 = seleksi_orang_tua(populasi, nilai_fitness)
        p2 = seleksi_orang_tua(populasi, nilai_fitness)
        c1, c2 = crossover(p1, p2, probabilitas_crossover)
        populasi_baru.append(mutasi(c1, probabilitas_mutasi))
        populasi_baru.append(mutasi(c2, probabilitas_mutasi))
        
    populasi = populasi_baru[:ukuran_populasi]


nilai_fitness_final = [hitung_fitness(ind, barang, kapasitas_tas) for ind in populasi]
best_index = nilai_fitness_final.index(max(nilai_fitness_final))
best_individu = populasi[best_index]

selected_items = [barang[i][0] for i in range(len(best_individu)) if best_individu[i] == 1]
selected_value = hitung_fitness(best_individu, barang, kapasitas_tas)
selected_weight = sum([barang[i][2] for i in range(len(best_individu)) if best_individu[i] == 1])

print("\n==========================================")
print("     HASIL OPTIMASI ALGORITMA GENETIKA    ")
print("==========================================")
print(f"Nilai Fitness Terbaik : {selected_value}")
print(f"Total Bobot Barang    : {selected_weight} (Maksimal {kapasitas_tas})")
print("Barang yang terpilih  :")
for item in selected_items:
    print(f"  - {item}")
print("==========================================\n")

print("Menampilkan grafik visualisasi... (Tutup jendela grafik untuk selesai)")
plt.figure(figsize=(10, 6))

for g in range(jumlah_generasi):
    plt.scatter([g]*ukuran_populasi, semua_fitness_individu[g], color='gray', alpha=0.3, s=15)

plt.plot(history_fitness_terbaik, color='blue', label='Fitness Tertinggi', linewidth=2)
plt.plot(history_fitness_rata_rata, color='red', label='Rerata Fitness', linewidth=2)
plt.plot(history_fitness_terendah, color='orange', label='Fitness Terendah', linewidth=2)

plt.title('Grafik Hasil Percobaan Algoritma Genetika Pertemuan 9')
plt.xlabel('Generasi')
plt.ylabel('Nilai Fitness')
plt.legend()
plt.grid(True)
plt.show()