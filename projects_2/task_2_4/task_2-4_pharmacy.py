number_of_capsules = int(input("Введите общее количество произведенных капсул: "))
capacity_of_one_package = int(input("Введите вместимость одной упаковки: "))
full_packages = number_of_capsules // capacity_of_one_package
capsules_remain = number_of_capsules % capacity_of_one_package

print("\n--- Отчет фасовочного цеха ---")
print(f"Полных упаковок: {full_packages}")
print(f"Остаток капсул: {capsules_remain}")