/*
Enter your query here.
*/
SELECT 
    Concat(Name, '(', LEFT(Occupation, 1), ')')
FROM
    occupations

order By
    Name;


SELECT 
    Concat('There are a total of ', COUNT(Name), ' ',lower(Occupation), 's.')
FROM
    Occupations

Group By 
    Occupation
Order By
    COUNT(Name);
