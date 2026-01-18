Q1.
docker run -it \
    --rm \
    --entrypoint=bash \       
    python:3.13

pip --version

Q2. Select the service's composite name as the host name and the docker container's port as the correction port

Q3. SELECT COUNT(*) FROM green_taxi_data WHERE lpep_pickup_datetime >= '2025-11-01' AND lpep_pickup_datetime < '2025-12-01' AND t
 rip_distance <= 1;

Q4. WITH bt AS (SELECT DATE(lpep_pickup_datetime) AS pickup_date, trip_distance FROM green_taxi_data WHERE trip_distance < 100), 
 bt1 AS (SELECT pickup_date, COUNT(trip_distance) AS tot_trip_miles FROM bt GROUP BY pickup_date) SELECT * FROM bt1 ORDER BY tot_trip_miles DESC;

 Q5. SELECT gtd."PULocationID", tzl."Zone", SUM(gtd.total_amount) AS total_pu_count FROM green_taxi_data gtd INNER JOIN taxi_zone_lookup tzl ON gtd."PULocationID" = tzl."LocationID" WHERE DATE(gtd.lpep_pickup_datetime) = '2025-11-18' GROUP BY gtd."PULocationID", tzl."Zone" ORDER BY total_pu_count DESC LIMIT 1;

 Q6. SELECT tzl_pu."Zone" AS pick_zone, tzl_do."Zone" AS drop_zone, MAX(gtd.tip_amount) AS 
 MAX_tip FROM green_taxi_data gtd INNER JOIN taxi_zone_lookup tzl_pu ON gtd."PULocationID" = tzl_pu."LocationID" INNER JOIN taxi_zone_lookup tzl_do ON gtd."DOLocationID" = tzl_do."LocationID" WHERE DATE(lpep_pickup_datetime) BETWEEN '2025-11-01' AND '2025-11-30' AND tzl_pu."Zone" = 'East Harlem North' GROUP BY tzl_pu."Zone", tzl_do."Zone" ORDER BY max_tip DESC LIMIT 5;