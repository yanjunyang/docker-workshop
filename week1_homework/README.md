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