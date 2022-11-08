# Задача № 1

cook_book = {}

with open("recipes.txt", "rt", encoding="utf-8") as file:

    for line in file:
        dish_name = line.strip()
        ingredients_count = int(file.readline())
        ingredients = []
        for _ in range(ingredients_count):
            ingredient = file.readline().strip().split(" | ")
            ingredient_name, quantity, measure = ingredient
            ingredients.append({"ingredient_name" : ingredient_name, "quantity" : int(quantity), "measure" : measure})
        file.readline()
        dishes = {dish_name : ingredients}
        cook_book.update(dishes)

    print(f"cook_book =\n "
          f"{cook_book}\n")

# Задача № 2

def get_shop_list_by_dishes(dishes, person_count):
    menu_count = {}
    for dish, ingredients in cook_book.items():
        for ingredient in ingredients:
            name = ingredient.get('ingredient_name')
            ingredient.pop('ingredient_name')
            if name not in menu_count.keys() :
                menu_count[name] = ingredient
                ingredient['quantity'] *= person_count
            else :
                ingredient['quantity'] += ingredient['quantity']

    print(menu_count)
    return


get_shop_list_by_dishes(["Омлет", "Запеченный картофель"], 2)

# Задача № 3
import os.path

sort_name = {}
name_text = {}

for file in os.listdir("sorted"):
    with open(os.path.join("sorted", file), 'rt', encoding="utf-8") as file:
        text = file.readlines()
        sort_name[file] = len(text)
        name_text[file] = text

sort_name = dict(sorted(sort_name.items(), key=lambda x: x[1]))

with open(os.path.join("sorted", "final.txt"), "w+", encoding="utf-8") as file:
    for key, value in sort_name.items():
        file.write(f"{key}\n")
        file.write(f"{value}\n")
        for line in name_text[key]:
            file.write(f"{line.strip()}\n")

















