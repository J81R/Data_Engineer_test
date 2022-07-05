SELECT TO_CHAR(payment_ts,'YYYY-MM') date, SUM(amount) amount_per_month,
SUM(SUM(amount)) OVER(ORDER BY TO_CHAR(payment_ts,'YYYY-MM')) cumulative_amount_per_month,
AVG(SUM(amount)) OVER(ORDER BY TO_CHAR(payment_ts,'YYYY-MM')) running_avg
FROM payment p
GROUP BY date