# After Create database
# 1.create user table

# CREATE TABLE IF NOT EXISTS users (
# 	user_id INTEGER PRIMARY KEY,
# 	first_name Text NOT NULL,
# 	car_ids 
# );

# 2.create car table
# CREATE TABLE IF NOT EXISTS cars (
# 	car_id INTEGER PRIMARY KEY,
# 	car_name Text NOT NULL
# );

# 3. create car_user table
# CREATE TABLE IF NOT EXISTS user_cars (
# 	user_car_id INTEGER,
# 	user_id INTEGER,
# 	car_id INTEGER,
# 	PRIMARY KEY (user_car_id),
# 	FOREIGN KEY (user_id)
# 		REFERENCES users (user_id)
# 			ON DELETE CASCADE
# 			ON UPDATE NO ACTION,
# 	FOREIGN KEY (car_id)
# 		REFERENCES cars (card_id)
# 			ON DELETE CASCADE
# 			ON UPDATE NO ACTION
# );

# Insert user data
# INSERT INTO users VALUES (Null, 'Rick');
# INSERT INTO users VALUES (Null, 'John');
# INSERT INTO users VALUES (Null, 'Zing');
# INSERT INTO users VALUES (Null, 'Nan');


# Insert cars data
# INSERT INTO cars VALUES (Null, 'Corvette Z06');
# INSERT INTO cars VALUES (Null, ' Lotus Exite S');
# INSERT INTO cars VALUES (Null, 'BMW M3');
# INSERT INTO cars VALUES (Null, 'BMW 320d');
# INSERT INTO cars VALUES (Null, 'Mercedes SLK AMG');
# INSERT INTO cars VALUES (Null, 'Toyota Alphard');
# INSERT INTO cars VALUES (Null, 'Toyota Camry');
# INSERT INTO cars VALUES (Null, 'Porsche 911');
# INSERT INTO cars VALUES (Null, ' BMW M5');
# INSERT INTO cars VALUES (Null, 'Jaguar');
# INSERT INTO cars VALUES (Null, 'TukTuk');
# INSERT INTO cars VALUES (Null, 'Mini Cooper');
# INSERT INTO cars VALUES (Null, 'Honda Jazz');


# Insert user_cars data
# INSERT INTO user_cars VALUES (NULL, 1, 2);
# INSERT INTO user_cars VALUES (NULL,1, 3);
# INSERT INTO user_cars VALUES (NULL,1, 4);
# INSERT INTO user_cars VALUES (NULL,2, 5);
# INSERT INTO user_cars VALUES (NULL,2, 6);
# INSERT INTO user_cars VALUES (NULL,3, 7);
# INSERT INTO user_cars VALUES (NULL,3, 1);
# INSERT INTO user_cars VALUES (NULL,4, 8);
# INSERT INTO user_cars VALUES (NULL,4, 9);
# INSERT INTO user_cars VALUES (NULL,4, 10);
# INSERT INTO user_cars VALUES (NULL,4, 11);
# INSERT INTO user_cars VALUES (NULL,4, 12);
# INSERT INTO user_cars VALUES (NULL,4, 13);
# INSERT INTO user_cars VALUES (NULL,4, 14);


# Question 5 get data like
# Rick, Corvette Z06
# Rick, Lotus Exite S
# Rick, BMW M3
# John, BMW 320d
# John, Mercedes SLK AMG
# Zing, Toyota Alphard
# Zing, Mercedes Sprinter
# Nan, Toyota Camry
# Nan, Porsche 911
# Nan, BMW M5
# Nan, Jaguar
# Nan, TukTuk
# Nan, Mini Cooper
# Nan, Honda Jazz
