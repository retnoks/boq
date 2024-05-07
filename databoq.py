import psycopg2
def get_connection():
    try:
        return psycopg2.connect(
            database="postgres",
            user="postgres",
            password="Rk5432",
            host="localhost",
            port=5432,
        )
    except psycopg2.Error as e:
        print("Error:", e)
        return None

conn = get_connection()
if conn:
    print("Connection to the PostgreSQL established successfully.")
else:
    print("Connection to the PostgreSQL encountered an error.")
    
import csv
with open('Data boq.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

import pandas as pd

df = pd.read_csv('Data boq.csv')
print(df)

vendors = df['vendor_name'].unique()
print(vendors)

boq_df = df.groupby(['vendor_name', 'month']).agg({
    'plan_progress': 'sum',
    'actual_progress': 'sum'
}).reset_index()
boq_df['plan_progress'] *= 15000
boq_df['actual_progress'] *= 15000
boq_df['month'] = pd.to_datetime(boq_df['month'])
boq_df['month'] = boq_df['month'].dt.strftime('%B %Y')
print(boq_df)

vendoralfatih_data = boq_df[boq_df['vendor_name'] == 'PT Vendor Al Fatih']
print(vendoralfatih_data)

import matplotlib.pyplot as plt

plt.plot(vendoralfatih_data['month'], vendoralfatih_data['plan_progress'], label='Plan Progress')
plt.plot(vendoralfatih_data['month'], vendoralfatih_data['actual_progress'], label='Actual Progress')
total_plan_per_month = vendoralfatih_data.groupby('month')['plan_progress'].sum()
total_actual_per_month = vendoralfatih_data.groupby('month')['actual_progress'].sum()
max_threshold = (total_plan_per_month.max() + total_actual_per_month.max()) / 2
plt.axhline(y=max_threshold, color='r', linestyle='--', label='Max Threshold')
plt.xlabel('Time')
plt.ylabel('Progress')
plt.title(f'PT Vendor Al Fatih Performance Analysis')
plt.tight_layout()
plt.legend()
plt.show()

vendorsejati_data = boq_df[boq_df['vendor_name'] == 'PT Vendor Sejati']
print(vendorsejati_data)

plt.plot(vendorsejati_data['month'], vendorsejati_data['plan_progress'], label='Plan Progress')
plt.plot(vendorsejati_data['month'], vendorsejati_data['actual_progress'], label='Actual Progress')
max_threshold = (total_plan_per_month.max() + total_actual_per_month.max()) / 2
plt.axhline(y=max_threshold, color='r', linestyle='--', label='Max Threshold')
plt.xlabel('Time')
plt.ylabel('Progress')
plt.title(f'PT Vendor Sejati Performance Analysis')
plt.tight_layout()
plt.legend()
plt.show()

berca_data = boq_df[boq_df['vendor_name'] == 'PT. Berca Engineering']
print(berca_data)

plt.plot(berca_data['month'], berca_data['plan_progress'], label='Plan Progress')
plt.plot(berca_data['month'], berca_data['actual_progress'], label='Actual Progress')
total_plan_per_month = berca_data.groupby('month')['plan_progress'].sum()
total_actual_per_month = berca_data.groupby('month')['actual_progress'].sum()
max_threshold = (total_plan_per_month.max() + total_actual_per_month.max()) / 2
plt.axhline(y=max_threshold, color='r', linestyle='--', label='Max Threshold')
plt.xlabel('Time')
plt.ylabel('Progress')
plt.title(f'PT. Berca Engineering Performance Analysis')
plt.xticks(rotation=90)
plt.tight_layout()
plt.legend()
plt.show()

fadiljaya_data = boq_df[boq_df['vendor_name'] == 'PT. Fadil Jaya abadi']
print(fadiljaya_data)

plt.plot(fadiljaya_data['month'], fadiljaya_data['plan_progress'], label='Plan Progress')
plt.plot(fadiljaya_data['month'], fadiljaya_data['actual_progress'], label='Actual Progress')
total_plan_per_month = fadiljaya_data.groupby('month')['plan_progress'].sum()
total_actual_per_month = fadiljaya_data.groupby('month')['actual_progress'].sum()
max_threshold = (total_plan_per_month.max() + total_actual_per_month.max()) / 2
plt.axhline(y=max_threshold, color='r', linestyle='--', label='Max Threshold')
plt.xlabel('Time')
plt.ylabel('Progress')
plt.title(f'PT. Fadil Jaya Abadi Performance Analysis')
plt.tight_layout()
plt.legend()
plt.show()

jayaabadi_data = boq_df[boq_df['vendor_name'] == 'PT. JAYA ABADI']
print(jayaabadi_data)

plt.plot(jayaabadi_data['month'], jayaabadi_data['plan_progress'], label='Plan Progress')
plt.plot(jayaabadi_data['month'], jayaabadi_data['actual_progress'], label='Actual Progress')
total_plan_per_month = jayaabadi_data.groupby('month')['plan_progress'].sum()
total_actual_per_month = jayaabadi_data.groupby('month')['actual_progress'].sum()
max_threshold = (total_plan_per_month.max() + total_actual_per_month.max()) / 2
plt.axhline(y=max_threshold, color='r', linestyle='--', label='Max Threshold')
plt.xlabel('Time')
plt.ylabel('Progress')
plt.title(f'PT. Jaya Abadi Performance Analysis')
plt.tight_layout()
plt.legend()
plt.show()

kalirayasari_data = boq_df[boq_df['vendor_name'] == 'PT. Kaliraya Sari']
print(kalirayasari_data)

plt.plot(kalirayasari_data['month'], kalirayasari_data['plan_progress'], label='Plan Progress')
plt.plot(kalirayasari_data['month'], kalirayasari_data['actual_progress'], label='Actual Progress')
total_plan_per_month = kalirayasari_data.groupby('month')['plan_progress'].sum()
total_actual_per_month = kalirayasari_data.groupby('month')['actual_progress'].sum()
max_threshold = (total_plan_per_month.max() + total_actual_per_month.max()) / 2
plt.axhline(y=max_threshold, color='r', linestyle='--', label='Max Threshold')
plt.xlabel('Time')
plt.ylabel('Progress')
plt.title(f'PT. Kaliraya Sari Performance Analysis')
plt.xticks(rotation=90)
plt.tight_layout()
plt.legend()
plt.show()

yaopyaya_data = boq_df[boq_df['vendor_name'] == 'PT. Yaop yaya op op ']
print(yaopyaya_data)

plt.plot(yaopyaya_data['month'], yaopyaya_data['plan_progress'], label='Plan Progress')
plt.plot(yaopyaya_data['month'], yaopyaya_data['actual_progress'], label='Actual Progress')
total_plan_per_month = yaopyaya_data.groupby('month')['plan_progress'].sum()
total_actual_per_month = yaopyaya_data.groupby('month')['actual_progress'].sum()
max_threshold = (total_plan_per_month.max() + total_actual_per_month.max()) / 2
plt.axhline(y=max_threshold, color='r', linestyle='--', label='Max Threshold')
plt.xlabel('Time')
plt.ylabel('Progress')
plt.title(f'PT. Yaop Yaya Op Op Performance Analysis')
plt.xticks(rotation=90)
plt.tight_layout()
plt.legend()
plt.show()

scm_data = boq_df[boq_df['vendor_name'] == 'SCM']
print(scm_data)

plt.plot(scm_data['month'], scm_data['plan_progress'], label='Plan Progress')
plt.plot(scm_data['month'], scm_data['actual_progress'], label='Actual Progress')
total_plan_per_month = scm_data.groupby('month')['plan_progress'].sum()
total_actual_per_month = scm_data.groupby('month')['actual_progress'].sum()
max_threshold = (total_plan_per_month.max() + total_actual_per_month.max()) / 2
plt.axhline(y=max_threshold, color='r', linestyle='--', label='Max Threshold')
plt.xlabel('Time')
plt.ylabel('Progress')
plt.title(f'SCM Performance Analysis')
plt.xticks(rotation=90)
plt.tight_layout()
plt.legend()
plt.show()

universal_data = boq_df[boq_df['vendor_name'] == 'Universal export']
print(universal_data)

plt.plot(universal_data['month'], universal_data['plan_progress'], label='Plan Progress')
plt.plot(universal_data['month'], universal_data['actual_progress'], label='Actual Progress')
total_plan_per_month = universal_data.groupby('month')['plan_progress'].sum()
total_actual_per_month = universal_data.groupby('month')['actual_progress'].sum()
max_threshold = (total_plan_per_month.max() + total_actual_per_month.max()) / 2
plt.axhline(y=max_threshold, color='r', linestyle='--', label='Max Threshold')
plt.xlabel('Time')
plt.ylabel('Progress')
plt.title(f'Universal Export Performance Analysis')
plt.xticks(rotation=90)
plt.tight_layout()
plt.legend()
plt.show()

yes_data = boq_df[boq_df['vendor_name'] == 'pt yes']
print(yes_data)

plt.plot(yes_data['month'], yes_data['plan_progress'], label='Plan Progress')
plt.plot(yes_data['month'], yes_data['actual_progress'], label='Actual Progress')
max_threshold = (total_plan_per_month.max() + total_actual_per_month.max()) / 2
plt.axhline(y=max_threshold, color='r', linestyle='--', label='Max Threshold')
plt.xlabel('Time')
plt.ylabel('Progress')
plt.title(f'PT Yes Performance Analysis')
plt.tight_layout()
plt.legend()
plt.show()