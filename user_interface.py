import re


def hello_line():
    print("Добро пожаловать в клиентскую базу данных!")


def get_task():
    print("Что вы хотите сделать?")
    print("1 - посмотреть все данные в базе")
    print("2 - посмотреть данные по клиенту")
    print("3 - добавить нового клиента")
    print("4 - редактировать данные в базе")
    print("5 - удалить данные из базы")
    print("0 - выход из базы")
    try:
        task = int(input("Введите Ваш выбор: "))
        while task > 5 or task < 0:
            print(f'Произошла ошибка при вводе данных, необходимо ввести число от 0 до 5')
            print("Попробуйте внести данные еще раз")
            task = int(input("Введите Ваш выбор: "))
        return task
    except ValueError:
        print(f'Произошла ошибка при вводе данных, необходимо ввести число от 0 до 5')
        print("Попробуйте еще раз")
        get_task()


# def get_file_key():
#     print(
#         "По какому значению вы хотите найти контрагента?\n \
#         1 - id компании \n \
#         2 - наименование компании \n \
#         3 - ИНН\n \
#         4 - отрасль\n \
#         5 - город\n \
#         6 - адрес\n \
#         7 - контактный номер телефона компании\n \
#         8 - контактный email\n \
#         9 - вернуться в предыдущее меню\n \
#         0 - выход"
#         )
#     try:
#         task = int(input("Введите Ваш выбор: "))
#         while task > 9 or task < 0:
#             print(f'Произошла ошибка при вводе данных, необходимо ввести число от 0 до 9')
#             print("Попробуйте внести данные еще раз")
#             task = int(input("Введите Ваш выбор: "))
#         return task
#     except ValueError:
#         print(f'Произошла ошибка при вводе данных, необходимо ввести число от 0 до 9')
#         print("Попробуйте еще раз")
#         get_file_key()


def get_find_data():
    return print("По какому значению будем искать запись?")


def get_reduct_data():
    return print("Какое значение будем менять?")


def get_file_key():
    print("1 - id компании")
    print("2 - наименование компании")
    print("3 - ИНН")
    print("4 - отрасль")
    print("5 - город")
    print("6 - адрес")
    print("7 - контактный номер телефона компании")
    print("8 - контактный email")
    print("9 - вернуться в предыдущее меню")
    print("0 - выход")
    try:
        task = int(input("Введите Ваш выбор: "))
        while task > 9 or task < 0:
            print(f'Произошла ошибка при вводе данных, необходимо ввести число от 0 до 9')
            print("Попробуйте внести данные еще раз")
            task = int(input("Введите Ваш выбор: "))
        return task
    except ValueError:
        print(f'Произошла ошибка при вводе данных, необходимо ввести число от 0 до 9')
        print("Попробуйте еще раз")
        get_file_key()


def get_data_id():
    try:
        id_number = int(input("Введите id компании: "))
        return id_number
    except ValueError:
        print(f'Произошла ошибка при вводе данных, необходимо ввести число')
        print("Попробуйте еще раз")
        get_data_id()


def get_company_name():
    return input("Введите наименование компании: ")


def get_data_inn():
    try:
        inn = int(input("Введите ИНН компании: "))
        return inn
    except ValueError:
        print(f'Произошла ошибка при вводе данных, необходимо ввести число')
        print("Попробуйте еще раз")
        get_data_id()


def get_data_industry():
    print(
        "Выбирите отрасль компании:\n \
        1 - промышленность \n \
        2 - сельское хозяйство \n \
        3 - недвижимость\n \
        4 - здравоохранение и медицина\n \
        5 - научная деятельность\n \
        6 - оптовая торговля\n \
        7 - юридические и бухгалтерские услуги\n \
        8 - транспортные услуги\n \
        9 - образование\n \
        10 - другая"
    )
    try:
        task = int(input("Введите Ваш выбор: "))
        while task > 10 or task < 0:
            print(f'Произошла ошибка при вводе данных, необходимо ввести число от 0 до 10')
            print("Попробуйте внести данные еще раз")
            task = int(input("Введите Ваш выбор: "))
        return task
    except ValueError:
        print(f'Произошла ошибка при вводе данных, необходимо ввести число от 0 до 10')
        print("Попробуйте еще раз")
        get_data_industry()


def get_data_city():
    return input("Введите город расположения компании: ")


def get_data_address():
    return input("Введите адрес компании: ")


def get_contact_phone():
    try:
        number = int(input("Введите контактный телефон (должен начинаться с цифры): "))
        return number
    except ValueError:
        print(f'Произошла ошибка при вводе данных, необходимо ввести число')
        print("Попробуйте еще раз")
        get_contact_phone()


def get_contact_email():
    email = input("Введите электронную почту: ")
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, email):
        return email
    else:
        print(f'Произошла ошибка при вводе данных, электронная почта должна содержать @')
        print("Попробуйте внести данные еще раз")
        get_contact_email()


def print_data1(find_key):
    print(f'Найденные данные со значением {find_key}:')
