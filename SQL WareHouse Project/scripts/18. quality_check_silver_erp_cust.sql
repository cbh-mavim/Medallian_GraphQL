SELECT DISTINCT
bdate
FROM silver.erp_cust_az12
WHERE bdate < '1924-01-01' OR bdate >GETDATE();


SELECT DISTINCT
gen
FROM silver.erp_cust_az12;