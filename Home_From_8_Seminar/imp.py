# ввод сотрудника

from datetime import datetime


import datetime
def record():
    entry=[]
    last_name = input('\nВведите Фамилию: ')
    entry.append(last_name.title())
    name = input('Введите Имя: ')
    entry.append(name.title())
    sur_name = input('Введите Отчество: ')
    entry.append(sur_name)
    dt = datetime.datetime.now()
    entry.insert(0,dt.strftime('%H:%M - %d.%m.%Y year'))
    print('Вами введена запись: ', entry)
    return entry