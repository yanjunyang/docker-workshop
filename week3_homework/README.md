-- Create an external table using the Yellow Taxi Trip Records
CREATE OR REPLACE EXTERNAL TABLE `dtc-de-course-484501.week3_homework.external_yellow_tripdata`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://week3-homework-bk-2981/yellow_tripdata_2024-*.parquet']
);

-- Create a (regular/materialized) table in BQ using the Yellow Taxi Trip Records
CREATE OR REPLACE TABLE `dtc-de-course-484501.week3_homework.yellow_tripdata`
AS
SELECT * FROM `dtc-de-course-484501.week3_homework.external_yellow_tripdata`;

-- Q1
SELECT COUNT(1) FROM `dtc-de-course-484501.week3_homework.yellow_tripdata`;

-- Q2
SELECT COUNT(DISTINCT(PULocationID)) FROM `dtc-de-course-484501.week3_homework.external_yellow_tripdata`;
SELECT COUNT(DISTINCT(PULocationID)) FROM `dtc-de-course-484501.week3_homework.yellow_tripdata`;

-- Q3
SELECT PULocationID FROM `dtc-de-course-484501.week3_homework.yellow_tripdata`;
SELECT PULocationID, DOLocationID FROM `dtc-de-course-484501.week3_homework.yellow_tripdata`;

-- Q4
SELECT COUNT(1) FROM `dtc-de-course-484501.week3_homework.yellow_tripdata` WHERE fare_amount = 0;

-- Q5
CREATE TABLE `dtc-de-course-484501.week3_homework.yellow_tripdata_partitioned`
PARTITION BY DATE(tpep_dropoff_datetime)
CLUSTER BY VendorID
AS SELECT * FROM `dtc-de-course-484501.week3_homework.yellow_tripdata`;

-- Q6
SELECT DISTINCT(VendorID)
FROM `dtc-de-course-484501.week3_homework.yellow_tripdata`
WHERE DATE(tpep_dropoff_datetime) BETWEEN '2024-03-01' AND '2024-03-15';

SELECT DISTINCT(VendorID)
FROM `dtc-de-course-484501.week3_homework.yellow_tripdata_partitioned`
WHERE DATE(tpep_dropoff_datetime) BETWEEN '2024-03-01' AND '2024-03-15';