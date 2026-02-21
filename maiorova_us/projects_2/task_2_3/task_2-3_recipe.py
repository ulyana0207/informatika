name_of_the_nutrient_medium = input('Введите название питательной среды: ')
agar_concentration = input('Введите концентрация агар-агара (%): ')
temperature_of_sterilization = input('Введите температуру стерелизации (°C): ')

with open("recipe.txt", "w", encoding="utf-8") as recipe:
    recipe.write(f"{name_of_the_nutrient_medium}\n\n")
    recipe.write(f"Концентрация агар-агара: {agar_concentration}\n")
    recipe.write(f"Температура стерелизации: {temperature_of_sterilization}\n")
print("\nФайл 'recipe.txt' успешно сформирован!")