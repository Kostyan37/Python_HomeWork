
def choice() -> int:
    print("\n" + "=" * 20)
    print("Выберите необходимое действие")
    print("1. Добавить сотрудника")
    print("2. Найти сотрудника ")
    print("3. Сделать выборку сотрудников по должности")
    print("4. Сделать выборку сотрудников по зарплате")
    print("5. Удалить сотрудника")
    print("6. Обновить данные сотрудника")
    print("7. Экспортировать данные в формате json")
    print("8. Экспортировать данные в формате cmv")
    print("9. Закончить работу")
    return int(input("Введите номер необходимого действия: "))

# fields = ["id", "last_name", "first_name", "position", "phone_number", "salary"]