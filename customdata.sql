DROP PROCEDURE IF EXISTS GetAllUserRestrictions;
DROP PROCEDURE IF EXISTS GetUnderSpecficCalorieCount;

/* Data Entry */

INSERT INTO measurement (measurement_name) VALUES ("Cup");
INSERT INTO measurement (measurement_name) VALUES ("Teaspoon");
INSERT INTO measurement (measurement_name) VALUES ("Tablespoon");
INSERT INTO measurement (measurement_name) VALUES ("Pound");
INSERT INTO measurement (measurement_name) VALUES ("Quart");
INSERT INTO measurement (measurement_name) VALUES ("Ounce");
INSERT INTO measurement (measurement_name) VALUES ("Pint");
INSERT INTO measurement (measurement_name) VALUES ("Millilitre");
INSERT INTO measurement (measurement_name) VALUES ("Litre");

INSERT INTO userrestriction (restriction_name) VALUES("Diabeties");
INSERT INTO userrestriction (restriction_name) VALUES("Hypertension");
INSERT INTO userrestriction (restriction_name) VALUES("Muslim");
INSERT INTO userrestriction (restriction_name) VALUES("Hindu");
INSERT INTO userrestriction (restriction_name) VALUES("Vegetarian");
INSERT INTO userrestriction (restriction_name) VALUES("Vegan");
INSERT INTO userrestriction (restriction_name) VALUES("Lactose Intolerant");
INSERT INTO userrestriction (restriction_name) VALUES("Peanut Allergy");
INSERT INTO userrestriction (restriction_name) VALUES("Egg Allergy");
INSERT INTO userrestriction (restriction_name) VALUES("Wheat Allergy");
INSERT INTO userrestriction (restriction_name) VALUES("Fish Allergy");
INSERT INTO userrestriction (restriction_name) VALUES("Shellfish Allergy");

/* Procedures */

DELIMITER //
CREATE PROCEDURE GetAllUserRestrictions(IN firstname varchar(255), IN lastname varchar(255))
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