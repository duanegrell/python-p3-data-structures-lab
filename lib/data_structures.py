spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    spicy_food_names = [food["name"] for food in spicy_foods]
    print (spicy_food_names)
    return (spicy_food_names)

# get_names(spicy_foods)

def get_spiciest_foods(spicy_foods):
    spicy_food_dictionary = [food for food in spicy_foods if food["heat_level"] > 5]
    print (spicy_food_dictionary)
    return (spicy_food_dictionary)

# get_spiciest_foods(spicy_foods)

def print_spicy_foods(spicy_foods):
    for i in range(len(spicy_foods)):
        name = spicy_foods[i]["name"]
        cuisine = spicy_foods[i]["cuisine"]
        heat_level = spicy_foods[i]["heat_level"]
        peppers = "🌶" * heat_level
        print (f'{name} ({cuisine}) | Heat Level: {peppers}')

# print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):

    for i in range(len(spicy_foods)):
        if spicy_foods[i]["cuisine"] == cuisine:
            print (spicy_foods[i])
            return (spicy_foods[i])

# get_spicy_food_by_cuisine(spicy_foods, "Thai")

def print_spiciest_foods(spicy_foods):
    for i in range(len(spicy_foods)):
        name = spicy_foods[i]["name"]
        cuisine = spicy_foods[i]["cuisine"]
        heat_level = spicy_foods[i]["heat_level"]
        peppers = "🌶" * heat_level

        if heat_level > 5:
            print (f'{name} ({cuisine}) | Heat Level: {peppers}')

# print_spiciest_foods(spicy_foods)

def get_average_heat_level(spicy_foods):

    heat_list = [food["heat_level"] for food in spicy_foods]
    avg_heat = int (sum(heat_list) / len(heat_list))
    print (avg_heat)
    return (avg_heat)

# get_average_heat_level(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):

    spicy_foods.append(spicy_food)
    print (spicy_foods)
    return (spicy_foods)

create_spicy_food(
    spicy_foods,
    {
        'name': 'Griot',
        'cuisine': 'Haitian',
        'heat_level': 10,
    }
)
