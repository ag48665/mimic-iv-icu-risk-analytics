import pandas as pd
from pathlib import Path

RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")

PROCESSED_DIR.mkdir(exist_ok=True)

# Load datasets
patients = pd.read_csv(RAW_DIR / "patients.csv.gz")
admissions = pd.read_csv(RAW_DIR / "admissions.csv.gz")
icustays = pd.read_csv(RAW_DIR / "icustays.csv.gz")
diagnoses = pd.read_csv(RAW_DIR / "diagnoses_icd.csv.gz")

# Keep only smaller subsets for portfolio project
patients_subset = patients.head(5000)
admissions_subset = admissions.head(5000)
icustays_subset = icustays.head(5000)
diagnoses_subset = diagnoses.head(5000)

# Save processed files
patients_subset.to_csv(PROCESSED_DIR / "patients_subset.csv", index=False)
admissions_subset.to_csv(PROCESSED_DIR / "admissions_subset.csv", index=False)
icustays_subset.to_csv(PROCESSED_DIR / "icustays_subset.csv", index=False)
diagnoses_subset.to_csv(PROCESSED_DIR / "diagnoses_subset.csv", index=False)

print("MIMIC-IV subset created successfully.")