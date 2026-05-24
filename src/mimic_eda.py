import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# Connect to database
conn = sqlite3.connect("database/mimic_icu.db")

# Load tables
patients = pd.read_sql("SELECT * FROM patients", conn)
admissions = pd.read_sql("SELECT * FROM admissions", conn)
icustays = pd.read_sql("SELECT * FROM icustays", conn)

# =========================
# ICU Length of Stay
# =========================

plt.figure(figsize=(8,5))
icustays['los'].hist(bins=30)
plt.title("ICU Length of Stay Distribution")
plt.xlabel("Length of Stay")
plt.ylabel("Frequency")
plt.savefig("outputs/icu_los_distribution.png")

# =========================
# Mortality Analysis
# =========================

mortality_counts = admissions['hospital_expire_flag'].value_counts()

plt.figure(figsize=(6,6))
mortality_counts.plot(kind='pie', autopct='%1.1f%%')
plt.title("Hospital Mortality Distribution")
plt.ylabel("")
plt.savefig("outputs/mortality_distribution.png")

# =========================
# ICU Care Unit Analysis
# =========================

unit_counts = icustays['first_careunit'].value_counts()

plt.figure(figsize=(10,6))
unit_counts.plot(kind='bar')
plt.title("ICU Stays by Care Unit")
plt.xlabel("Care Unit")
plt.ylabel("Total ICU Stays")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("outputs/icu_unit_analysis.png")

print("EDA visualizations created successfully.")

conn.close()