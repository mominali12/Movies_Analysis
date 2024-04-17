-- Docs: https://docs.mage.ai/guides/sql-blocks
CREATE OR REPLACE TABLE dtc-de-410416.imdb_dataset.imdb_data_partitioned 
PARTITION BY DATE_TRUNC(release_date, YEAR)
AS
SELECT * FROM {{df1}};