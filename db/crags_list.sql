DROP TABLE IF EXISTS routes;
DROP TABLE IF EXISTS crags;
DROP TABLE IF EXISTS locations;

CREATE TABLE locations (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE crags (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    location_id INT REFERENCES locations(id)
);

CREATE TABLE routes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    grade VARCHAR(255),
    climbed BOOLEAN,
    crag_id INT REFERENCES crags(id)
);

INSERT INTO locations (name)
Values ('North West, Scotland');

INSERT INTO locations (name)
Values ('North East, Scotland');

INSERT INTO locations (name)
Values ('South West, Scotland');

INSERT INTO locations (name)
Values ('South East, Scotland');

INSERT INTO locations (name)
Values ('Peak District, England');



INSERT INTO crags (name, location_id)
VALUES ('Bennybeg', 2);

INSERT INTO crags (name, location_id)
VALUES ('Dumbarton Rock Sector 1', 3);

INSERT INTO crags (name, location_id)
VALUES ('Dumbarton Rock Sector 2', 3);

INSERT INTO routes (name, grade, crag_id)
VALUES ('Angels Pavement', 'f5', 2);

INSERT INTO routes (name, grade, crag_id)
VALUES ('Monsoon Gully', 'S 4b', 2);

INSERT INTO routes (name, grade, crag_id)
VALUES ('Jims Traverse', 'S', 1);

INSERT INTO routes (name, grade, crag_id)
VALUES ('Benydorm', '5a', 1);