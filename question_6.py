
Question 6
# Using the same database from Question 6, write an SQL query that returns the following report:

# Rick, 3
# Zing, 2
# Nan, 7
# John, 2

SELECT 
	first_name as name,
	count(*) as count_car
FROM user_cars 
INNER JOIN users ON users.user_id = user_cars.user_id 
GROUP BY user_cars.user_id
## use count(*) as count_car for show count number of user and use group by to group user_id and count 

