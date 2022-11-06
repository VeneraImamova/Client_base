import csv
import user_interface as us
import choices as ch
import os

company_id = 0


def write_data():
    global company_id
    with open('data_base.csv', 'a', encoding='utf-8', newline='') as myfile:
        writer = csv.writer(myfile, delimiter=";", quoting=csv.QUOTE_MINIMAL)
        writer.writerow(
            [company_id, us.get_company_name(), us.get_data_inn(), us.get_data_industry(), us.get_data_city(),
             us.get_data_address(), us.get_contact_phone(), us.get_contact_email()])
        company_id += 1
        return print("Данные успешно записаны")


def print_data():
    data = open('data_base.csv', 'r', encoding='utf-8')
    reader = csv.DictReader(data, delimiter=";", quotechar='"')
    for row in reader:
        print(row['ID компании'], row['Название компании'], row['ИНН'], row['Отрасль'], row['Город'], row['Адрес'],
              row['Контактный телефон'], row['Электронная почта'])


def change_data():
    with open('data_base.csv', 'r', encoding='utf-8') as my_file:
        reader = csv.DictReader(my_file, delimiter=";", quotechar='"')
        row_name, find_string = ch.choice_file_key(us.get_file_key())
        for row in reader:
            if find_string == row[row_name]:
                us.print_data1(find_string)
                print(row['ID компании'], row['Название компании'], row['ИНН'], row['Отрасль'], row['Город'],
                      row['Адрес'], row['Контактный телефон'], row['Электронная почта'])
        with open('temp.csv', 'w', encoding='utf-8', newline='') as new_file:
            header = ['ID компании', 'Название компании', 'ИНН', 'Отрасль', 'Город',
                      'Адрес', 'Контактный телефон', 'Электронная почта']
            writer = csv.DictWriter(new_file, fieldnames=header, delimiter=";")
            writer.writeheader()
            for line in reader:
                if find_string != line[row_name]:
                    writer.writerow(line)
                else:
                    new_row, new_data = ch.choice_file_key(us.get_file_key())
                    row[new_row] = new_data
                    temp = [row['ID компании'], row['Название компании'], row['ИНН'], row['Отрасль'], row['Город'],
                            row['Адрес'], row['Контактный телефон'], row['Электронная почта']]
                    writer.writerow(temp)
    os.remove('data_base.csv')
    os.rename('temp.csv', 'data_base.csv')



def show_data():
    data = open('data_base.csv', 'r', encoding='utf-8')
    reader = csv.DictReader(data, delimiter=";", quotechar='"')
    row_name, find_string = ch.choice_file_key(us.get_file_key())
    for row in reader:
        if find_string == row[row_name]:
            us.print_data1(find_string)
            print(row['ID компании'], row['Название компании'], row['ИНН'], row['Отрасль'], row['Город'], row['Адрес'],
                  row['Контактный телефон'], row['Электронная почта'])

        else:
            print("Данные не были найдены")




def delete_data():
    with open('data_base.csv', 'r', encoding='utf-8') as my_file:
        reader = csv.DictReader(my_file, delimiter=";", quotechar='"')
        row_name, find_string = ch.choice_file_key(us.get_file_key())
        for row in reader:
            if find_string == row[row_name]:
                us.print_data1(find_string)
                print(row['ID компании'], row['Название компании'], row['ИНН'], row['Отрасль'], row['Город'],
                      row['Адрес'], row['Контактный телефон'], row['Электронная почта'])
        with open('temp.csv', 'w', encoding='utf-8', newline='') as new_file:
            header = ['ID компании', 'Название компании', 'ИНН', 'Отрасль', 'Город',
                              'Адрес', 'Контактный телефон', 'Электронная почта']
            writer = csv.DictWriter(new_file, fieldnames=header, delimiter=";")
            writer.writeheader()
            for line in reader:
                if find_string != line[row_name]:
                    writer.writerow(line)
    os.remove('data_base.csv')
    os.rename('temp.csv', 'data_base.csv')

