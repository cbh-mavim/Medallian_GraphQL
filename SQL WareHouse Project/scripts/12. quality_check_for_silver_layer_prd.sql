--Quality Check of Silver Layer

--Check for Duplicate in Primary Key
--Expectation : No Results
SELECT * FROM silver.crm_prd_info;
SELECT
prd_id,
COUNT(*)
FROM silver.crm_prd_info
GROUP BY prd_id
HAVING COUNT(*) > 1 OR prd_id IS NULL;

SELECT prd_nm
FROM silver.crm_prd_info
WHERE prd_nm != TRIM(prd_nm);


SELECT prd_cost
FROM silver.crm_prd_info
WHERE prd_cost < 0 OR prd_cost IS NULL;


SELECT DISTINCT prd_line
FROM silver.crm_prd_info;


SELECT *
FROM silver.crm_prd_info
WHERE prd_end_dt< prd_start_dt;