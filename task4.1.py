def sal():
    try:
        time = float(input('Выработка в часах '))
        salary = int(input('Ставка в руб. '))
        bonus = int(input('Премия в руб. '))
        res = time * salary + bonus
        print(f'заработная плата сотрудника  {res}')
    except ValueError:
        return print('Not a number')
def sal()
