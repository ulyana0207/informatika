donor = input("Введите фенотип группы крови донора (I, II, III, IV): ").strip().upper()
recipient = input("Введите фенотип группы крови реципиента (I, II, III, IV): ").strip().upper()
if donor == recipient:
    print(f"ПЕРЕЛИВАНИЕ ВОЗМОЖНО")
elif donor == "I":
    print(f"ПЕРЕЛИВАНИЕ ВОЗМОЖНО")
elif patient == "IV":
    print(f"ПЕРЕЛИВАНИЕ ВОЗМОЖНО")
else:
    print(f"ПЕРЕЛИВАНИЕ НЕВОЗМОЖНО")