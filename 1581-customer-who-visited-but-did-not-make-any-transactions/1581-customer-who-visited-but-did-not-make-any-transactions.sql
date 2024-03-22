# Write your MySQL query statement below
select Visits.customer_id,count(visits.visit_id) as count_no_trans  from  Visits
left join Transactions on Visits.visit_id=Transactions.visit_id WHERE transaction_id IS NULL
group by customer_id ;