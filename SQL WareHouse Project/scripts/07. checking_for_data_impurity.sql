--Check for Nulls or Duplicate in the Primary Key--
--Expectation : No Result--
SELECT cst_firstname
FROM bronze.crm_cust_info
WHERE cst_firstname != TRIM(cst_firstname);


SELECT cst_lastname
FROM bronze.crm_cust_info
WHERE cst_lastname != TRIM(cst_lastname);


SELECT 
cst_id,
COUNT(*)
FROM bronze.crm_cust_info
GROUP BY cst_id
HAVING COUNT(*) > 1 OR cst_id IS NULL;

SELECT DISTINCT cst_gndr
FROM bronze.crm_cust_info;


SELECT DISTINCT cst_material_status
FROM bronze.crm_cust_info;