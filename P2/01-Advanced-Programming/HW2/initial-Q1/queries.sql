-- Section1
   select country, count(*) as count
   from salary
   group by country
   order by count desc
   limit 3;
-- Section2
   select `Job Title`, round(avg(Salary), 2) as avg_salary
   from salary
   where Senior=1
   group by `Job Title`
   order by avg_salary desc, `Job Title`
   limit 5;
-- Section3
    select gender, count(*) as count,
           round(AVG(age), 2) as avg_age,
           round(AVG(`Years of Experience`), 2) as avg_exp
    from salary
    where Senior = 0 and salary >= 50000
    group by gender;
-- Section4
    select ROUND(AVG(age), 2) AS avg_age_usa
    from salary
    where Senior=0 and `Years of Experience` >= 10 and `Education Level`=3 and country = 'USA';

