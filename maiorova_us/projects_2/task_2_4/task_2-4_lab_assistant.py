solution_volume = float(input('Введите объем раствора (в мл): '))
weight = solution_volume * 0.009
water_volume = solution_volume

with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write(f"ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n")
    file.write("-" * 23 + "\n\n")
    file.write(f"Общий объем: {solution_volume} мл\n")
    file.write(f"Масса соли:  {weight} г\n")
    file.write(f"Объем воды:  {water_volum} мл\n")

    priint('Рецепт успешно сохранен в файл recipe.txt')