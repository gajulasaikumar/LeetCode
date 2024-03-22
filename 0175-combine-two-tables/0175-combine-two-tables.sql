# Write your MySQL query statement belowsele

select p.firstName, p.lastName ,a.city,a.state from person as p left join address as a on
p.personId=a.personId ;