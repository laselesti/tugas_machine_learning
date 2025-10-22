import pandas as pd
import seaborn as sns
import csv

# === Membaca dataset kelulusan ===
df = pd.read_csv("kelulusan_mahasiswa.csv")

print(df.info())
print(df.head())

# === Cek data kosong dan duplikat ===
print(df.isnull().sum())
df = df.drop_duplicates()

# === Visualisasi sederhana ===
sns.boxplot(x=df['IPK'])

# === Membuat file data_karyawan.csv ===
data = [
    ["id_karyawan", "nama", "jabatan", "gaji"],
    [1, "Andi", "Manager", 7000000],
    [2, "Budi", "Staff Admin", 4500000],
    [3, "Citra", "HRD", 5000000],
    [4, "Dinda", "Marketing", 4800000]
]

with open("data_karyawan.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("✅ File data_karyawan.csv berhasil dibuat!")


