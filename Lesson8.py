# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

def save_contact():
    with open('Phonebook.txt', 'a', encoding='utf-8') as file:
        file.writelines(str(input('введите фамилию ')) + '\n')
        file.writelines(str(input('введите имя '))+ '\n')
        file.writelines(str(input('введите отчество '))+ '\n')
        file.writelines(str(input('введите номер телефона '))+ '\n' + '\n')
        print('Контакт успешно сохранен!')

def search(surname, name=''):
    with open('Phonebook.txt', 'r', encoding='utf-8') as file:
        if name == '': # если поиск ведется только по фамилии
            while True:
                if file.readline() == surname + '\n':
                    print(surname)
                    for i in range(4):
                        print(file.readline().replace('\n', ''))
                    break
                if not file.readline():
                    print('Такого контакта нет в списке')
                    break

        else: # поиск по имени и фамилии
            while True:
                if file.readline() == surname + '\n': 
                    if file.readline() == name + '\n':
                        print(surname)
                        print(name)
                        for i in range(3):
                            print(file.readline().replace('\n', ''))
                        break
                if not file.readline():
                    print('Такого контакта нет в списке')
                    break

def interface():
    mode = str(input('введите режим работы со справочником (импорт или экспорт): '))
    if mode == 'импорт': save_contact()
    elif mode == 'экспорт': search(input('введите фамилию для поиска: '), input('введите имя для поиска, или оставьте поле пустым: '))
    else: 
        print('введены некорректные данные, попробуйте еще раз')
        interface()

interface()


