SELECT COUNT(*) FROM dtc-de-course-484501.dbt_prod.fct_monthly_zone_revenue;

SELECT 
  pickup_zone,
  SUM(revenue_monthly_total_amount) AS revenue_total_amount_year
FROM dtc-de-course-484501.dbt_prod.fct_monthly_zone_revenue
WHERE service_type = 'Green' 
  AND EXTRACT(YEAR FROM revenue_month) = 2020
GROUP BY pickup_zone
ORDER BY revenue_total_amount_year DESC;

SELECT
  COUNT(*)
FROM dtc-de-course-484501.dbt_prod.fct_trips
WHERE service_type = 'Green' AND FORMAT_TIMESTAMP('%Y-%m', pickup_datetime) = '2019-10';

