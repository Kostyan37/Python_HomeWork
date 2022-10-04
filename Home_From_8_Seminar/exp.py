# поиск сотрудника

def search():
    print('По какому параметру поиск: \n\
        1 - Фамилия;\n\
        2 - Имя;\n\
        3 - Отчетство;\n')
    a = int(input('Ваш выбор: '))
    if a == 1:
        entry = input('Введите Фамилию: ').title()
    if a == 2:
        entry = input('Введите Имя: ').title()
    if a == 3:
        entry = input('Введите Отчество: ')
      
    print('Поиск по : ', entry)
    return 