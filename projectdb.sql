DROP TABLE IF EXISTS plan_generate;
DROP TABLE IF EXISTS plan_meal_day;
DROP TABLE IF EXISTS use_recipe;
DROP TABLE IF EXISTS limits;
DROP TABLE IF EXISTS user_has_condition;
DROP TABLE IF EXISTS follow_instruction;
DROP TABLE IF EXISTS use_ingredients;
DROP TABLE IF EXISTS within_kitchen;
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS mealplan;
DROP TABLE IF EXISTS mealplanday;
DROP TABLE IF EXISTS recipe;
DROP TABLE IF EXISTS usercondition;
DROP TABLE IF EXISTS instruction;
DROP TABLE IF EXISTS ingredient;
DROP TABLE IF EXISTS measurement;
DROP TABLE IF EXISTS kitchen;

CREATE TABLE user(
user_id INT(11) NOT NULL UNIQUE AUTO_INCREMENT,
user_firstname VARCHAR(255) NOT NULL,
user_lastname VARCHAR(255) NOT NULL,
user_address VARCHAR(255) NOT NULL,
user_email VARCHAR(255) NOT NULL,
user_password VARCHAR(255) NOT NULL,
user_phonenumber VARCHAR(20) NOT NULL,
user_image VARCHAR(255) NOT NULL,
user_dob DATE NOT NULL,
PRIMARY KEY(user_id)
);

CREATE TABLE mealplan(
mealplan_id INT(11) NOT NULL UNIQUE AUTO_INCREMENT,
PRIMARY KEY (mealplan_id)
);

CREATE TABLE mealplanday(
mealplanday_id INTEGER(11) NOT NULL UNIQUE AUTO_INCREMENT,
day VARCHAR(30) NOT NULL,
mealtype VARCHAR(50) NOT NULL,
PRIMARY KEY(mealplanday_id)
);

CREATE TABLE recipe(
recipe_id INT(11) NOT NULL UNIQUE AUTO_INCREMENT,
recipe_type VARCHAR(50) NOT NULL,
recipe_image VARCHAR(255) NOT NULL,
recipe_serving DECIMAL(11,2) NOT NULL,
recipe_creationdate DATE NOT NULL,
recipe_caloriecount DECIMAL(11,2) NOT NULL,
PRIMARY KEY(recipe_id)
);

CREATE TABLE usercondition(
condition_id INT(11) NOT NULL UNIQUE AUTO_INCREMENT,
condition_name VARCHAR(50) NOT NULL,
PRIMARY KEY(condition_id)
);

CREATE TABLE instruction(
instruction_id INT(11) NOT NULL UNIQUE AUTO_INCREMENT,
instruction_details VARCHAR(255) NOT NULL,
PRIMARY KEY(instruction_id)
);

CREATE TABLE measurement(
measurement_id INT(11) NOT NULL UNIQUE AUTO_INCREMENT,
measurement_name VARCHAR(30) NOT NULL,
PRIMARY KEY(measurement_id)
);

CREATE TABLE ingredient(
ingredient_id INT(11) NOT NULL UNIQUE AUTO_INCREMENT,
ingredient_name VARCHAR(255) NOT NULL,
ingredient_measurement DECIMAL(11,2) NOT NULL,
ingredient_type VARCHAR(30) NOT NULL,
PRIMARY KEY(ingredient_id)
);

CREATE TABLE kitchen(
kitchen_id INT(11) NOT NULL UNIQUE AUTO_INCREMENT,
PRIMARY KEY(kitchen_id)
);

CREATE TABLE plan_generate(
user_id INT (11) NOT NULL,
mealplan_id INT(11) NOT NULL,
PRIMARY KEY(user_id, mealplan_id),
FOREIGN KEY(user_id) references user(user_id) on update cascade on delete cascade,
FOREIGN KEY(mealplan_id) references mealplan(mealplan_id) on update cascade on delete restrict
);

CREATE TABLE plan_meal_day(
mealplan_id INT (11) NOT NULL,
mealplanday_id INT (11) NOT NULL,
PRIMARY KEY(mealplan_id, mealplanday_id),
FOREIGN KEY(mealplan_id) references mealplan(mealplan_id) on update cascade on delete cascade,
FOREIGN KEY(mealplanday_id) references mealplanday(mealplanday_id) on update cascade on delete restrict
);

CREATE TABLE use_recipe(
mealplanday_id INT (11) NOT NULL,
recipe_id INT (11) NOT NULL,
PRIMARY KEY (mealplanday_id, recipe_id),
FOREIGN KEY(mealplanday_id) references mealplanday(mealplanday_id) on update cascade on delete cascade,
FOREIGN KEY(recipe_id) references recipe(recipe_id) on update cascade on delete restrict
);

CREATE TABLE user_has_condition(
user_id INT (11) NOT NULL,
condition_id INT(11) NOT NULL,
PRIMARY KEY (user_id, condition_id),
FOREIGN KEY(user_id) references user(user_id) on update cascade on delete cascade,
FOREIGN KEY(condition_id) references usercondition(condition_id) on update cascade on delete restrict
);

CREATE TABLE limits(
condition_id INT (11) NOT NULL,
ingredient_id INT (11) NOT NULL,
PRIMARY KEY (condition_id, ingredient_id),
FOREIGN KEY(condition_id) references usercondition(condition_id) on update cascade on delete cascade,
FOREIGN KEY(ingredient_id) references ingredient(ingredient_id) on update cascade on delete restrict
);

CREATE TABLE follow_instruction(
recipe_id INT (11) NOT NULL,
instruction_id INT(11) NOT NULL,
instruction_order INT(11) NOT NULL,
PRIMARY KEY (recipe_id, instruction_id),
FOREIGN KEY(recipe_id) references recipe(recipe_id) on update cascade on delete cascade,
FOREIGN KEY(instruction_id) references instruction(instruction_id) on update cascade on delete restrict
);

CREATE TABLE use_ingredients(
recipe_id INT(11) NOT NULL,
ingredient_id INT (11) NOT NULL,
ingredient_quantity DECIMAL(11,2) NOT NULL,
PRIMARY KEY (recipe_id, ingredient_id),
FOREIGN KEY(recipe_id) references recipe(recipe_id) on update cascade on delete cascade,
FOREIGN KEY(ingredient_id) references ingredient(ingredient_id) on update cascade on delete restrict
);

CREATE TABLE within_kitchen(
ingredient_id INT(11) NOT NULL,
kitchen_id INT (11) NOT NULL,
PRIMARY KEY(ingredient_id, kitchen_id),
FOREIGN KEY(ingredient_id) references ingredient(ingredient_id) on update cascade on delete cascade,
FOREIGN KEY(kitchen_id) references kitchen(kitchen_id) on update cascade on delete restrict
);