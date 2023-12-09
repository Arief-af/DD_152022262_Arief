import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)

# no 1
for index, row in df.iterrows():
    df.at[index, 'Gaji_plus_5%'] = row['Gaji'] * 1.05

#no 2
print("DataFrame setelah peningkatan gaji 5%:")
print(df)

print("\nRingkasan Perubahan:")
print("Gaji setiap karyawan ditingkatkan sebesar 5%.")

# no 3
for index, row in df.iterrows():
    df.at[index, 'Gaji_plus_2%'] = (lambda x: x * 1.02 if row['Usia'] > 30 else x)(row['Gaji_plus_5%'])

# no 4
print("\nDataFrame setelah peningkatan gaji tambahan:")
print(df)

print("\nRingkasan Hasil:")
print("Gaji setiap karyawan ditingkatkan sebesar 5%.")
print("Karyawan di atas 30 tahun mendapatkan peningkatan tambahan sebesar 2%.")
