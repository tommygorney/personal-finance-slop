select   strftime("%Y-%m", date) AS 'Date', strftime('%m', date) as 'Month', Category, amount
from sftransactions

select   *
from sftransactions
order by date, description, amount

select   sum(amount)
from sftransactions
where date > '2025-01-01'

select   strftime('%m', date) as 'Month', Category, sum(Amount)
from sftransactions
group by  strftime('%m', date), Category



select   strftime('%m', date) as 'Month', Category, sum(Amount)
from sftransactions
where Category = 'Income'
group by  strftime('%m', date), Category;

select   strftime('%m', date) as 'Month', 'Spending' as Spending , sum(Amount)
from sftransactions
where Category <> 'Income'
group by  strftime('%m', date);

select strftime('%Y-%m', date) AS 'Date', ROUND(sum(Amount), 2) as 'Balance' from sftransactions group by  strftime('%Y-%m', date);

select strftime('%Y-%m', date) AS 'Date', sum(CASE WHEN amount < 0 THEN Amount ELSE 0 END) AS 'Spending', sum(CASE WHEN amount > 0 THEN Amount ELSE 0 END) AS 'Income', ROUND(sum(Amount), 2) as 'Balance' from sftransactions group by strftime('%Y-%m', date);



select   strftime("%Y-%m", date) AS 'Date', ROUND(sum(Amount), 2) as 'Balance' from sftransactions where Amount > 0 group by  strftime("%Y-%m", date);

strftime("%Y-%m", 'MD')

