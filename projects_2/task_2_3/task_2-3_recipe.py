name_of_the_nutrient_medium = input('Введите название питательной среды: ')
agar_concentration = input('Введите концентрация агар-агара (%): ')
temperature_of_sterilization = input('Введите температуру стерелизации (°C): ')

with open("C:/Презентации/информатика/projects_2/task_2_3/recipe.txt", "w", encoding="utf-8") as recipe:
    recipe.write(f"{name_of_the_nutrient_medium}\n")
    recipe.write(f"Концентрация {name_of_the_nutrient_medium}: {agar_concentration}\n")
    recipe.write(f"Температура стерелизации: {temperature_of_sterilization}\n")
print("\nФайл 'recipe.txt' успешно сформирован!")