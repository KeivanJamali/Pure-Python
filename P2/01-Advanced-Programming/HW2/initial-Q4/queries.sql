-- Section1
    SELECT id
    FROM Users
    WHERE LENGTH(name) = 9 AND name LIKE '_l%'
    ORDER BY id;
-- Section2
    SELECT SUM(price) AS total_price
    FROM Orders o
             JOIN Deliveries d ON d.id = o.delivery_id
    WHERE YEAR(requested_at) between '2021-01-01' AND '2021-12-31';
-- Section3
    SELECT driver_id
    FROM Deliveries d
             JOIN Rates r ON r.delivery_id = d.id
    GROUP BY driver_id
    ORDER BY AVG(rate) DESC, driver_id
        LIMIT 10;
    -- Section4
    SELECT Deliveries.id AS delivery_id, driver_id
    FROM Deliveries
    WHERE TIMEDIFF(delivered_at, requested_at) >= '04:00:00'
    ORDER BY delivery_id;
-- Section5
SELECT u.name, u.phone
FROM Users u
         INNER JOIN (
    SELECT d.user_id
    FROM Deliveries d
    WHERE ST_Distance_Sphere(
                  POINT(
                          CAST(CONV(SUBSTRING(d.src, 17, 16), 16, 10) AS DECIMAL(10,6)),
                          CAST(CONV(SUBSTRING(d.src, 1, 16), 16, 10) AS DECIMAL(10,6))
                  ),
                  POINT(
                          CAST(CONV(SUBSTRING(d.dest, 17, 16), 16, 10) AS DECIMAL(10,6)),
                          CAST(CONV(SUBSTRING(d.dest, 1, 16), 16, 10) AS DECIMAL(10,6))
                  )
          ) >= 20000 -- Assuming the distance is in meters
    GROUP BY d.user_id
    HAVING COUNT(*) >= 5
) sub ON u.id = sub.user_id
ORDER BY u.name;