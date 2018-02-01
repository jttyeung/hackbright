-- Include your solutions to the More Practice problems in this file.

-- Insert a Brand

INSERT INTO brands
  VALUES ('sub', 'Subaru', 1953, 'Tokyo, Japan');


-- Insert Models

INSERT INTO models (year, brand_id, name)
  VALUES (  2015,
            ( SELECT brand_id
              FROM brands
              WHERE name = 'Chevrolet'),
            'Malibu'
          );

INSERT INTO models (year, brand_id, name)
  VALUES (  2015,
            ( SELECT brand_id
              FROM brands
              WHERE name = 'Subaru'),
            'Outback'
          );


-- Create an Awards Table

CREATE TABLE awards(
  id SERIAL NOT NULL PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  year INT NOT NULL,
  winner_id INT REFERENCES models
  );

-- Insert Awards

INSERT INTO awards (name, year, winner_id)
  VALUES ('IIHS Safety Award',
          2015,
          ( SELECT model_id
            FROM models
            WHERE year = 2015
              AND name = 'Malibu')
          );

INSERT INTO awards (name, year, winner_id)
  VALUES ('IIHS Safety Award',
          2015,
          ( SELECT model_id
            FROM models
            WHERE year = 2015
              AND name = 'Outback')
         );

INSERT INTO awards (name, year)
  VALUES ('Best in Class',
          2015
          );







