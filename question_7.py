Question 7
# Using the same database from Question 6, write an SQL query that returns the records with
# more than 2 cars

# Rick, 3
# Nan, 7

SELECT 
	first_name as name,
	count(*) as count_car
FROM user_cars 
INNER JOIN users ON users.user_id = user_cars.user_id 
GROUP BY user_cars.user_id
HAVING count_car > 2

## from question 6 use HAVING count_car > 2 to find user has count of cars more two
