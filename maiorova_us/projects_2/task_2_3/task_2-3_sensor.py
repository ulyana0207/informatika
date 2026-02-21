operator_name = input('Введите имя оператора: ')
pressure_value = input('Введите текущее значение датчика давления (Па): ')
with open("sensor_log.txt", "w", encoding="utf-8") as sensor:
    sensor.write(f"ОПЕРАТОР\tЗНАЧЕНИЕ\n")
    sensor.write(f"{operator_name}\t{pressure_value}\n")
print('Данные успешно сохранены в sensor_log.txt')