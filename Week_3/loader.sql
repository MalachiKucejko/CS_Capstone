-- car_color
.mode csv
.import data/car_color.csv car_color

-- make_model
.mode csv
.import data/make_model.csv make_model

-- local_car
.mode csv
.import data/local_car.csv local_car

-- interstate_car
.mode csv
.import data/interstate_car.csv tmp_interstate_car

INSERT INTO interstate_car (observation_time, car_count)
SELECT observation_time, car_count FROM tmp_interstate_car;

DROP TABLE tmp_interstate_car;