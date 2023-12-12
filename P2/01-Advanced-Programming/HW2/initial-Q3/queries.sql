-- Section1
    SELECT year(STR_TO_DATE(date, '%m/%d/%Y')) as year, COUNT(*) AS count
    FROM matches
    GROUP BY year
    ORDER BY count DESC;
-- Section2
    SELECT
        home_team_continent,
        SUM(CASE WHEN (tournament = "Friendly" and home_team_result = "Win") THEN 1 ELSE 0 END) AS win_game,
        RANK() OVER (ORDER BY SUM(CASE WHEN (tournament = "Friendly" and home_team_result = "Win") THEN 1 ELSE 0 END) DESC) AS ranking
    FROM matches
    GROUP BY home_team_continent;
-- Section3
    SELECT MONTHNAME(STR_TO_DATE(date, '%m/%d/%Y')) as month, COUNT(*) AS count
    FROM matches
    WHERE home_team_result = "Lose"
    GROUP BY month
    ORDER BY count DESC
    LIMIT 3;
-- Section4
    SELECT
        away_team_continent,
        COUNT(*) AS count
    FROM matches
    WHERE away_team_fifa_rank BETWEEN 10 AND 50 and away_team_continent != home_team_continent
    GROUP BY away_team_continent
    ORDER BY count DESC;

