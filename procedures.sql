DROP PROCEDURE IF EXISTS RegisterUser;
DROP PROCEDURE IF EXISTS LoginUser;
DROP PROCEDURE IF EXISTS AddRecipe;
DROP PROCEDURE IF EXISTS GetAllUserRestrictions;
DROP PROCEDURE IF EXISTS GetUnderSpecficCalorieCount;

/* Procedures */

DELIMITER //
CREATE PROCEDURE RegisterUser(IN firstname VARCHAR(255),IN lastname VARCHAR(255),IN address VARCHAR(255),IN email VARCHAR(255),IN password VARCHAR(255),IN phonenumber VARCHAR(30),IN image VARCHAR(255),IN dob DATE)
BEGIN INSERT INTO user(user_firstname,user_lastname,user_address,user_email,user_password,user_phonenumber,user_image,user_dob) VALUES(firstname,lastname,address,email,password,phonenumber,image,dob);
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE LoginUser(IN email VARCHAR(255),IN password VARCHAR(255))
BEGIN (SELECT user.user_email from user WHERE user.user_email=email AND user.user_password=password
);
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE AddRecipe(IN name VARCHAR(120),IN recipetype VARCHAR(30),IN image VARCHAR(255),IN serving DECIMAL(11,2),IN preptime INT(11),IN creationdate DATE,IN caloriecount INT(11))
BEGIN INSERT INTO recipe(recipe_name,recipe_type, recipe_image, recipe_serving, recipe_preptime,recipe_creationdate,recipe_caloriecount) VALUES(name,recipetype,image,serving,preptime,creationdate,caloriecount);
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE GetAllUserRestrictions(IN firstname VARCHAR(255), IN lastname VARCHAR(255))
BEGIN (SELECT userrestriction.restriction_name
FROM user JOIN user_has_restriction JOIN userrestriction
ON user.user_id=user_has_restriction.user_id AND user_has_restriction.restriction_id=userrestriction.restriction_id
WHERE user.user_firstname=firstname AND user.user_lastname=lastname);
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE GetUnderSpecficCalorieCount(IN caloriecount INT(11))
BEGIN (SELECT recipe.recipe_name
FROM recipe
WHERE recipe.caloriecount <= caloriecount);
END //
DELIMITER ;