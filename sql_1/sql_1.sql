--I was not sure if you wanted the shortest movie for 'PG' as a separate query, I just added shortest_movie column for the entire result set

SELECT totals.*, 
	(SELECT title FROM film WHERE rating = totals.rating_category ORDER BY length ASC LIMIT 1) shortest_movie
FROM
  (
  SELECT rating  rating_category, AVG(length) avg_duration,
  MIN(MIN(length)) over (partition by rating) min_duration,
  MAX(MAX(length)) over (partition by rating) max_duration
  FROM film f
  GROUP BY rating_category
  ) totals

/*
SELECT title
FROM film
WHERE rating = 'PG'
ORDER BY length ASC
LIMIT 1
*/