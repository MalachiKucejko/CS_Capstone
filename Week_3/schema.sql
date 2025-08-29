-- car_color
DROP TABLE IF EXISTS car_color;
CREATE TABLE car_color (
    id INTEGER PRIMARY KEY,
    color TEXT NOT NULL
);

-- make_model
DROP TABLE IF EXISTS make_model;
CREATE TABLE make_model (
    id INTEGER PRIMARY KEY,
    make TEXT NOT NULL,
    model TEXT NOT NULL
);

-- local_car
DROP TABLE IF EXISTS local_car;
CREATE TABLE local_car (
    id INTEGER PRIMARY KEY,
    make_model_id INTEGER NOT NULL,
    car_color_id INTEGER NOT NULL,
    observation_time TIMESTAMP NOT NULL
);

-- interstate_car
DROP TABLE IF EXISTS interstate_car;
DROP TABLE IF EXISTS tmp_interstate_car;

CREATE TEMP TABLE tmp_interstate_car (
    observation_time TIMESTAMP NOT NULL,
    car_count INTEGER NOT NULL
);

CREATE TABLE interstate_car (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    observation_time TIMESTAMP NOT NULL,
    car_count INTEGER NOT NULL
);