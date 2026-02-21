full_name_researcher = input('Введите ФИО исследователя: ')
date = input('Введите дату: ')
name_experiment = input('Введите название эксперимента: ')
conclusion = input('Введите вывод: ')

with open("journal.txt", "w", encoding="utf-8") as journal:
    journal.write("+" + "-" * 50 + "+\n")
    journal.write("| Электронный лабораторный журнал |\n")
    journal.write("+" + "-" * 50 + "+\n")
    journal.write(f"| ФИО исследователя : {full_name_researcher} |\n")
    journal.write(f"| Дата              : {date}                 |\n")
    journal.write(f"| Эксперимент       : {name_experiment}      |\n")
    journal.write("+" + "-" * 50 + "+\n")
    journal.write(f"| Вывод:{' ' * 44}|\n")
    journal.write(f"| {conclusion} |\n")
    journal.write("+" + "-" * 50 + "+\n")

print("\nФайл 'journal.txt' успешно создан!")