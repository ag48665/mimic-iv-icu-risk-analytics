import pandas as pd
import sqlite3
from pathlib import Path

# Paths
PROCESSED_DIR = Path("data/processed")
DATABASE_DIR = Path("database")

DATABASE_DIR.mkdir(exist_ok=True)

# SQLite database
conn = sqlite3.connect(DATABASE_DIR / "mimic_icu.db")

# Load processed datasets
patients = pd.read_csv(PROCESSED_DIR / "patients_subset.csv")
admissions = pd.read_csv(PROCESSED_DIR / "admissions_subset.csv")
icustays = pd.read_csv(PROCESSED_DIR / "icustays_subset.csv")
diagnoses = pd.read_csv(PROCESSED_DIR / "diagnoses_subset.csv")

# Save to SQLite
patients.to_sql("patients", conn, if_exists="replace", index=False)
admissions.to_sql("admissions", conn, if_exists="replace", index=False)
icustays.to_sql("icustays", conn, if_exists="replace", index=False)
diagnoses.to_sql("diagnoses", conn, if_exists="replace", index=False)

print("SQLite database created successfully.")

conn.close()