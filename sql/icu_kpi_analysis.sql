-- =====================================
-- MIMIC-IV ICU KPI ANALYSIS
-- Real-world clinical data demo project
-- =====================================

-- 1. Total patients
SELECT
    COUNT(DISTINCT subject_id) AS total_patients
FROM patients;

-- 2. Total hospital admissions
SELECT
    COUNT(DISTINCT hadm_id) AS total_admissions
FROM admissions;

-- 3. Total ICU stays
SELECT
    COUNT(DISTINCT stay_id) AS total_icu_stays
FROM icustays;

-- 4. ICU length of stay summary
SELECT
    ROUND(AVG(los), 2) AS avg_icu_los,
    ROUND(MIN(los), 2) AS min_icu_los,
    ROUND(MAX(los), 2) AS max_icu_los
FROM icustays;

-- 5. Mortality rate based on hospital_expire_flag
SELECT
    COUNT(*) AS total_admissions,
    SUM(hospital_expire_flag) AS total_deaths,
    ROUND(100.0 * SUM(hospital_expire_flag) / COUNT(*), 2) AS mortality_rate_percent
FROM admissions;

-- 6. ICU stays by first care unit
SELECT
    first_careunit,
    COUNT(*) AS total_stays,
    ROUND(AVG(los), 2) AS avg_los
FROM icustays
GROUP BY first_careunit
ORDER BY total_stays DESC;