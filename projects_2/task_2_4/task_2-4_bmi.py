weight = float(input("Введите массу белков (г): "))
height = float(input("Введите ваш рост (см): "))
height = height / 100
bmi = weight / (height ** 2)

print("\n--- Отчет о состоянии здоровья ---")
print(f"Рост:\t\t\t{height} см")
print(f"Вес:\t\t\t{weight} кг")
print(f"Индекс массы тела:\t{bmi}")