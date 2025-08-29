SELECT 
    lc.id,
    mm.make,
    mm.model,
    cc.color,
    lc.observation_time
FROM local_car lc
LEFT JOIN make_model mm ON lc.make_model_id = mm.id
LEFT JOIN car_color cc ON lc.car_color_id = cc.id
WHERE DATE(lc.observation_time) = '2025-08-27' and (mm.make = 'Tesla'); 

-- find total number of entries in interstate_car on date and then sum car_count for that date
SELECT COUNT(*) AS total_entries
FROM interstate_car
WHERE date(observation_time) = '2025-08-28';

SELECT SUM(car_count) AS total_cars
FROM interstate_car
WHERE date(observation_time) = '2025-08-28';