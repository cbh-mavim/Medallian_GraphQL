--Check for Unwanted Spaces
--Expectation : No Results
SELECT cst_firstname
FROM silver.crm_cust_info
WHERE cst_firstname != TRIM(cst_firstname);


SELECT cst_lastname
FROM silver.crm_cust_info
WHERE cst_lastname != TRIM(cst_lastname);


SELECT 
cst_id,
COUNT(*)
FROM silver.crm_cust_info
GROUP BY cst_id
HAVING COUNT(*) > 1 OR cst_id IS NULL;

SELECT DISTINCT cst_gender
FROM silver.crm_cust_info;


SELECT DISTINCT cst_marital_status
FROM silver.crm_cust_info;