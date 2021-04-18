Python 3.9.4 (v3.9.4:1f2e3088f3, Apr  4 2021, 12:32:44) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> v = float(input("Введите выручку компании "))
c = float(input("Введите издержки компании "))
if v > c:
    print(f"Крмпания получает прибыль. Рентабельность выручки составила {v / c:.2f}")
    w = int(input("Введите количество сотрудников фирмы "))
    print(f"прибыль в расчете на одного сотрудника сотавила {v / w:.2f}")
elif profit == costs:
    print("Компания рентабельна")
else:
    print("Компания работает себе в убыток")