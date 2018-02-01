1

-----

Select all fields for all brands in the brands table.

The result set for this query should be every record in the brands table.

-----


SELECT * FROM brands;


==========
2

-----

Select all fields for all car models made by Pontiac in the
models table.

The result set should be:
 model_id | year | brand_id |    name    
----------+------+----------+------------
       24 | 1961 | pon      | Tempest
       26 | 1962 | pon      | Grand Prix
       35 | 1963 | pon      | Grand Prix
       41 | 1964 | pon      | LeMans
       42 | 1964 | pon      | Bonneville
       43 | 1964 | pon      | Grand Prix
(6 rows)


-----


SELECT * FROM models WHERE brand_id = 'pon';


==========
3

-----

Select the brand id and model name for all models made in
1964 from the models table.

The result set should be:
 brand_id |    name     
----------+-------------
 che      | Corvette
 for      | Mustang
 for      | Galaxie
 pon      | LeMans
 pon      | Bonneville
 pon      | Grand Prix
 ply      | Fury
 stu      | Avanti
 aus      | Mini Cooper
(9 rows)
 

-----


SELECT brand_id, name
FROM models
WHERE year = 1964;


==========
4

-----

Select the model name, brand name, and headquarters for
the Ford Mustang from the models and brands tables.

The result set should be:
 model_name | brand_name | headquarters 
------------+------------+--------------
 Mustang    | Ford       | Dearborn, MI
 (1 rows)


-----


SELECT models.name as model_name, brands.name as brand_name, headquarters
FROM models
JOIN brands
ON models.brand_id = brands.brand_id
WHERE models.name = 'Mustang'
AND brands.name = 'Ford';


==========
5

-----

Select all rows for the three oldest brands from the brands
table.

The result set should be:
 brand_id |    name    | founded |    headquarters     | discontinued 
----------+------------+---------+---------------------+--------------
 stu      | Studebaker |    1852 | South Bend, Indiana |         1967
 ram      | Rambler    |    1901 | Kenosha, Washington |         1969
 cad      | Cadillac   |    1902 | New York City, NY   |             
(3 rows)


-----


SELECT * FROM brands
ORDER BY founded
LIMIT 3;


==========
6

-----

Count the Ford models in the database. The output should be a
number.

The result set should be:
 count 
-------
     6
(1 row)


-----


SELECT count(models.name) as count
FROM models
JOIN brands
ON models.brand_id = brands.brand_id
WHERE brands.name = 'Ford';


==========
7

-----

Select the brand name of any and all car brands that are not
discontinued.

The result set should be:
   name    
-----------
 Ford
 Chrysler
 Citroen
 Chevrolet
 Cadillac
 BMW
 Buick
 Tesla
 Subaru
(9 rows)


-----


SELECT name FROM brands
WHERE discontinued IS NULL;


==========
8

-----

Select everything from rows 15-24 of the models table in
alphabetical order by name. The result set should have 10 records.

The result set should be:
 model_id | year | brand_id |   name   
----------+------+----------+----------
        6 | 1954 | che      | Corvette
        8 | 1955 | che      | Corvette
       10 | 1956 | che      | Corvette
       11 | 1957 | che      | Corvette
       13 | 1958 | che      | Corvette
       20 | 1960 | che      | Corvette
       38 | 1964 | che      | Corvette
       37 | 1963 | che      | Corvette
       25 | 1961 | che      | Corvette
       27 | 1962 | che      | Corvette
(10 rows)


-----


SELECT * from models
ORDER BY name
OFFSET 14
LIMIT 10;


==========
9

-----

Select the model year, name, and id, and the award name for all of the models from 1964 and beyond. Include row(s)
for model(s) even if they have not won awards.

Note that in the result set, the award name should be NULL if
the model is not in the awards table.

So, the result set should be:
 year |    name     | model_id |       name        
------+-------------+----------+-------------------
 2015 | Malibu      |       47 | IIHS Safety Award
 2015 | Outback     |       48 | IIHS Safety Award
 1964 | Mustang     |       39 | 
 1964 | Mini Cooper |       46 | 
 1964 | Galaxie     |       40 | 
 1964 | Corvette    |       38 | 
 1964 | Bonneville  |       42 | 
 1964 | LeMans      |       41 | 
 1964 | Fury        |       44 | 
 1964 | Avanti      |       45 | 
 1964 | Grand Prix  |       43 | 
(11 rows)


-----


SELECT models.year, models.name, model_id, awards.name
FROM models
LEFT JOIN awards
ON models.model_id = awards.winner_id
WHERE models.year >= 1964;


==========
10

-----

Modify the query so it only selects brands who have models.

-----


SELECT b.name, 
         m.year, 
         m.name 
FROM brands AS b
RIGHT JOIN models AS m
ON b.brand_id = m.brand_id 
  ORDER BY b.name;


==========
11

-----

Modify the query to add another field to the results that gives
the number of years from the year of the model until the brand becomes
discontinued.

Display this new field with the name years_until_brand_discontinued. The correct
result set is:

    name    |       name       | year | discontinued | years_until_brand_discontinued 
------------+------------------+------+--------------+--------------------------------
 Austin     | Mini             | 1959 |         1987 |                             28
 Austin     | Mini             | 1963 |         1987 |                             24
 Austin     | Mini Cooper      | 1961 |         1987 |                             26
 Austin     | Mini Cooper      | 1964 |         1987 |                             23
 Austin     | Mini Cooper S    | 1963 |         1987 |                             24
 Fairthorpe | Rockette         | 1960 |         1976 |                             16
 Hillman    | Minx Magnificent | 1950 |         1981 |                             31
 Plymouth   | Fury             | 1964 |         2001 |                             37
 Pontiac    | Bonneville       | 1964 |         2010 |                             46
 Pontiac    | Grand Prix       | 1962 |         2010 |                             48
 Pontiac    | Grand Prix       | 1963 |         2010 |                             47
 Pontiac    | Grand Prix       | 1964 |         2010 |                             46
 Pontiac    | LeMans           | 1964 |         2010 |                             46
 Pontiac    | Tempest          | 1961 |         2010 |                             49
 Rambler    | Classic          | 1963 |         1969 |                              6
 Studebaker | Avanti           | 1961 |         1967 |                              6
 Studebaker | Avanti           | 1962 |         1967 |                              5
 Studebaker | Avanti           | 1963 |         1967 |                              4
 Studebaker | Avanti           | 1964 |         1967 |                              3
(19 rows)

-----


SELECT b.name,
         m.name,
         m.year,
         b.discontinued,
	   b.discontinued - m.year as years_until_brand_discontinued
FROM models AS m
    LEFT JOIN brands AS b
      ON m.brand_id = b.brand_id
  WHERE b.discontinued IS NOT NULL
  ORDER BY b.name, m.name, m.year;


==========
12

-----

Write a query that selects the name and year founded for brands that do NOT have any
models in the models table.

The correct result set is:

 name  | founded
-------+---------
 Tesla |    2003
(1 rows)

-----


SELECT brands.name, founded
FROM brands
LEFT JOIN models
ON brands.brand_id = models.brand_id
WHERE model_id IS NULL;


==========
13

-----

Select the brand id of any brand with more than 5 models in the
database using a HAVING clause.

The correct result set is:

 brand_id 
----------
 che
 pon
 for
(3 rows)


-----


SELECT brand_id
FROM models
GROUP BY brand_id
HAVING count(brand_id) > 5;


==========
14

-----

Using a subquery, select the name and year of any model whose
year is the same year that ANY brand was founded.

The result set should be:

   name    | year 
-----------+------
 Imperial  | 1926
 Corvette  | 1953
 Corvette  | 1954
 Fleetwood | 1954
(4 rows)

-----


SELECT name, year
FROM models
WHERE year in (SELECT founded FROM brands);