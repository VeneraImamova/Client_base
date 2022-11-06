import user_interface as us
import work_with_data as w


def choice_task(choice):
    if choice == 1:
        return w.print_data()
    elif choice == 2:
        us.get_find_data()
        return w.show_data()
    elif choice == 3:
        return w.write_data()
    elif choice == 4:
        us.get_find_data()
        return w.change_data()
    elif choice == 5:
        us.get_find_data()
        return w.delete_data()
    elif choice == 0:
        quit(print("Спасибо за использование программы!=)"))
    else:
        error = 'Ошибка данных при пределении типа числа'
        print("Произошла ошибка, попробуйте воспользоваться программой еще раз")
        quit(error)


def choice_file_key(choice):
    if choice == 1:
        row = 'ID компании'
        find_data = us.get_data_id()
        return row, find_data
    elif choice == 2:
        row = 'Название компании'
        find_data = us.get_company_name()
        return row, find_data
    elif choice == 3:
        row = 'ИНН'
        find_data = us.get_data_inn()
        return row, find_data
    elif choice == 4:
        row = 'Отрасль'
        find_data = choice_industry(us.get_data_industry())
        return row, find_data
    elif choice == 5:
        row = 'Город'
        find_data = us.get_data_city()
        return row, find_data
    elif choice == 6:
        row = 'Адрес'
        find_data = us.get_data_address()
        return row, find_data
    elif choice == 7:
        row = 'Контактный телефон'
        find_data = us.get_contact_phone()
        return row, find_data
    elif choice == 8:
        row = 'Электронная почта'
        find_data = us.get_contact_email()
        return row, find_data
    elif choice == 9:
        return us.get_task()
    elif choice == 0:
        quit(print("Спасибо за использование программы!=)"))
    else:
        error = 'Ошибка данных при пределении типа числа'
        print("Произошла ошибка, попробуйте воспользоваться программой еще раз")
        quit(error)


def choice_industry(choice):
    if choice == 1:
        industry = 'промышленность'
        return industry
    elif choice == 2:
        industry = 'сельское хозяйство'
        return industry
    elif choice == 3:
        industry = 'недвижимость'
        return industry
    elif choice == 4:
        industry = 'здравоохранение и медицина'
        return industry
    elif choice == 5:
        industry = 'научная деятельность'
        return industry
    elif choice == 6:
        industry = 'оптовая торговля'
        return industry
    elif choice == 7:
        industry = 'юридические и бухгалтерские услуги'
        return industry
    elif choice == 8:
        industry = 'транспортные услуги'
        return industry
    elif choice == 9:
        industry = 'образование'
        return industry
    elif choice == 10:
        industry = input("Введите отрасль")
        return industry

