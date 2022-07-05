SELECT staff_member, SUM(rentals) rentals_2020 , SUM(amount) revenue_2020
FROM
	(
	SELECT s.last_name || ', ' || s.first_name staff_member, 1 rentals, NULL amount
	FROM staff s
	JOIN rental r on s.staff_id = r.staff_id and date_part('year',r.rental_ts) = 2020
	
	UNION ALL
	
	SELECT s.last_name || ', ' || s.first_name staff_member, NULL rentals, p.amount
	FROM staff s
	JOIN payment p on s.staff_id = p.staff_id and date_part('year',p.payment_ts) = 2020
	) sub_q
GROUP BY staff_member