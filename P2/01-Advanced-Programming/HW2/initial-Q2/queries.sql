-- Section1
    SELECT Year_of_Release AS Year, SUM(Run_Time_in_minutes) AS Total_Time
    FROM movies
    GROUP BY Year_of_Release
    ORDER BY Total_Time DESC;
-- Section2
    SELECT movie_name, Year_of_Release, Movie_Rating
    FROM movies
    ORDER BY
        CASE
            WHEN Year_of_Release >= 2000 THEN Movie_Rating
            ELSE 0 -- A large number to push movies before 2000 to the end
            END DESC,
        CASE
            WHEN Year_of_Release < 2000 THEN Year_of_Release
            ELSE 1 -- A small number to push movies before 2000 to the end
            END DESC,
        movie_name;
-- Section3
    SELECT movie_name, COALESCE(metascore, 0) AS metascore
    FROM movies
    ORDER BY metascore DESC, movie_name;
-- Section4
    SELECT ID, movie_name
    FROM movies
    WHERE movie_name LIKE 'The%' AND Year_of_Release IN (1999, 2018, 2001, 1990, 2005)
    ORDER BY movie_name;