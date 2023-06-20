import os

def show_contacts(file_name):
    os.system('CLS')
    with open(file_name, 'r') as file:
        data = file.readlines()
        for contact in data :
            print(contact, end='')
    print()
    input('\nНажмите "Enter"')       
    
def add_contact(file_name):
    os.system('CLS')
    with open(file_name, 'a') as file:
        res = ''
        res += input('Введите фамилию контакта: ') + ' '
        res += input('Введите имя контакта: ') + ' '
        res += input('Введите номер телефона: ' + "+7 ")

        file.write('\n' + res)
    print()
    input('\nКонтакт добавлен. Нажмите "Enter"')       
    
def search_contact(file_name):
    os.system('CLS')
    target = input('Введите имя для поиска контакта: ')

    with open(file_name, 'r') as file:
        contacts = file.readlines()
        for contact in contacts:
            if target in contact:
                print(contact)
                break
        else :
            print('Нет контакта с таким именем.') 
    print()
    input('\nНажмите "Enter"')       

def drawing():
    print('1 - Показать контакты')
    print('2 - Добавить контакт')
    print('3 - Поиск контакта')
    print('4 - Перезапись контакта')
    print('5 - Удаление контакта')
    print('6 - Выход')

def main(file_name):
    while True:
        os.system('CLS')
        drawing()
        user_choice = int(input('Введите номер пункта: '))

        if user_choice == 1 :
            show_contacts(file_name)
        elif user_choice == 2 :
            add_contact(file_name)
        elif user_choice == 3 :
            search_contact(file_name)
        elif user_choice == 4 :
            transform_contact(file_name)
        elif user_choice == 5 :
            delited_contact(file_name)
        elif user_choice == 6 :
            print('Хорошего дня!')
            return

def transform_contact(file_name):
    os.system('CLS')
    target = input('Введите имя для изменения контакта: ')

    with open(file_name, 'r') as file:
        contacts = file.readlines()
        for persona in list(enumerate(contacts)):
            if target in persona[1]:
                print(f'Будет изменен: {persona[1]}')
                res = ''
                res += input('Введите новую фамилию: ') + ' '
                res += input('Введите новое имя: ') + ' '
                res += input('Введите новый номер телефона: ')
                print(f"\nНовый контакт: {res}")
                contacts[persona[0]] = res + "\n"
                with open(file_name, "w") as file:
                    file.writelines(contacts)
                break
        else:
            print('Нет контакта с таким именем.')
    print()
    input('press any key.')

def delited_contact(file_name):
    os.system('CLS')
    target = input('Введите имя для удаления контакта: ')

    with open(file_name, 'r') as file:
        contacts = file.readlines()
        for persona in list(enumerate(contacts)):
            if target in persona[1]:
                print(f'Контакт {persona[1]} удален.')
                res = ''
                contacts[persona[0]] = res 
                with open(file_name, "w") as file:
                    file.writelines(contacts)
                break
        else:
            print('Нет контакта с таким именем.')
    print()
    input('\nНажмите "Enter"')

main("test.txt")

























