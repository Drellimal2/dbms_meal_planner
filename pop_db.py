from faker import Factory

ingredient_list = """asparagus
apples
avacado
alfalfa
acorn squash
almond
arugala
artichoke
applesauce
asian noodles
antelope
ahi tuna
albacore tuna
Apple juice
Avocado roll
Bruscetta
bacon
black beans
bagels
baked beans
BBQ
bison
barley
beer
bisque
bluefish
bread
broccoli
buritto
babaganoosh
Cabbage
cake
carrots
carne asada
celery
cheese
chicken
catfish
chips
chocolate
chowder
clams
coffee
cookies
corn
cupcakes
crab
curry
cereal
chimichanga
dates
dips
duck
dumplings
donuts
eggs
enchilada
eggrolls
English muffins
edimame
eel sushi
fajita
falafel
fish
franks
fondu
French toast
French dip
Garlic
ginger
gnocchi
goose
granola
grapes
green beans
Guancamole
gumbo
grits
Graham crackers
ham
halibut
hamburger
honey
huenos rancheros
hash browns
hot dogs
haiku roll
hummus
ice cream
Irish stew
Indian food
Italian bread
jambalaya
jelly / jam
jerky
jalapeño
kale
kabobs
ketchup
kiwi
kidney beans
kingfish
lobster
Lamb
Linguine
Lasagna
Meatballs
Moose
Milk
Milkshake
Noodles
Ostrich
Pizza
Pepperoni
Porter
Pancakes
Quesadilla
Quiche
Reuben
Spinach
Spaghetti
Tater tots
Toast
Venison
Waffles
Wine
Walnuts
Yogurt
Ziti
Zucchin
"""

fake = Factory.create()

BASE_INSERT = "INSERT INTO {} ({}) VALUES({});"

def generate_user(num):
	table = "user"
	fields = ['user_firstname', 'user_lastname', 'user_address', 'user_email', 'user_password', 'user_phonenumber', 'user_image', 'user_dob']
	image = "https://assets-cdn.github.com/images/modules/logos_page/Octocat.png"
	for x in range(num):
		vals = [fake.first_name(), fake.last_name(), fake.address(), fake.email(), "password", fake.phone_number(), image, fake.date()]

		print BASE_INSERT.format(table, ", ".join(fields), ", ".join(vals))

def generate_ingr():
	table = "ingredient"
	fields = ['ingredient_name', 'ingredient_type']
	types = ["meat", "spice", "veg", "dairy", "fruit"]
	ingredients = ingredient_list.split("\n")
	for x in range(len(ingredients)):
		vals = [ingredients[x], types[x%5]]
		print BASE_INSERT.format(table, ", ".join(fields), ", ".join(vals))
	
#generate_user(5)
generate_ingr()