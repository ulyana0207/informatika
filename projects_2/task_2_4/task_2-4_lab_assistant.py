solution_volume = float(input('Введите объем раствора (в мл): '))
weight = solution_volume * 0.009
water_volume = solution_volume

with open("C:/Презентации/информатика/projects_2/task_2_4/recipe.txt", "w", encoding="utf-8") as file:
    file.write(f"ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n")
    file.write("-" * 23 + "\n\n")
    file.write(f"Общий объем: {solution_volume} мл\n")
    file.write(f"Масса соли:  {weight} г\n")
    file.write(f"Объем воды:  {water_volume} мл\n")

    print('Рецепт успешно сохранен в файл recipe.txt')