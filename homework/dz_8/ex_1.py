#Создать телефонный справочник
# Фамилия Имя Отчество, номер телефона
def show_phonebook():
    #посмотреть содержимое справочника
        with open('phonebook.txt', 'r', encoding='utf-8') as file:
            book = file.read()#.split('\n')
        return book

def new_phonebook():
    #добавление в справочник
    with open('phonebook.txt', 'a', encoding='utf-8') as file:
        file.write(input('Введите новую строку: '+ '\n') )
    

def find_phonebook():
    #функция поиска
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        book = file.read().split('\n')
        temp = input('поиск: ')
        for i in book:
            if temp in i:
                print(i)


def delete_smth(name):
    #удалить данные
    persons = read_phonebook()
    with open("phonebook.txt", "w", encoding="utf8" ) as file:
        for person in persons:
            if name != person:
                file.write(person)

def change_smth(new_name, old_name):
    #Изменить данные
    persons = read_phonebook()
    with open("data.txt", "w", encoding="utf8" ) as file:
        for person in persons:
            if  old_name != person:
                file.write(person)
            else:
                file.write(new_name + "\n")



while True:
    mode = input('Выберите вариант работы' + '\n'
                  +'0-поиск, 1-чтение файла, 2-добавление в файл, 3-удаление, 4-замена, 5-выход: ')
    if mode == '1':
        print(show_phonebook())
    elif mode == '0':
        find_phonebook()
    elif mode == '2':
        new_phonebook()
    elif mode == '3':
        name = input('кого удаляем?: ')
        delete_smth(name)
    elif mode == '4':
        old_name = input('кого хотим переименовать?: ')
        new_name = input('как хотим его назвать?: ')
        change_smth(new_name,old_name)
    elif mode == '5':
        break
    else:
        print('No mode')
    