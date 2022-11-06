file = open('data_base.csv', 'w', encoding='utf-8', newline='')
newrecord = "ID компании;Название компании;ИНН;Отрасль;Город;Адрес;Контактный телефон;Электронная почта\n"
file.writelines(newrecord)
