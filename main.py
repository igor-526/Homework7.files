import os
def cookbook():
    cookbook_list = []
    cook_book = {}
    ROOT_PATH = os.getcwd()
    FILE_NAME = 'cookbook.txt'
    FILE_DIR = 'files'
    file_path = os.path.join(ROOT_PATH, FILE_DIR, FILE_NAME)
    with open(file_path) as cookbook:
       for line in cookbook:
           cookbook_list.append(line.strip())
    while len(cookbook_list) != 0:
        cook_book[cookbook_list[0]] = []
        for i in range (2, int(cookbook_list[1])+2):
           cook_book[cookbook_list[0]].append({'ingredient_name': cookbook_list[i].split(' | ')[0], 'quantity': int(cookbook_list[i].split(' | ')[1]), 'measure': cookbook_list[i].split(' | ')[2]})
        del cookbook_list[0:(int(cookbook_list[1])+3)]
    return (cook_book)
def menu(choise):
    while choise != 'q':
        print('1. Показать cookbook')
        print('2. Рассчитать список для покупок')
        print('q. Выход из программы')
        choise = input('Выберите пункт: ')
        if choise == '1':
            print(cookbook())
            print()
        elif choise == '2':
            print(shoplist(input("Введите через запятую с пробелом наименования блюд: ").split(', '), int(input("Введите количество персон: "))))
            print()
        else:
            if choise != 'q':
                print('Вы выбрали несуществующий пункт меню! Попробуйте ещё раз!')
                print()
    else:
        print('До свидания!')
def shoplist(dishes, person):
    cook_book = cookbook()
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ing_info in cook_book[dish]:
                if ing_info['ingredient_name'] in shop_list:
                    shop_list[ing_info['ingredient_name']]['quantity'] += ing_info['quantity']
                else:
                    shop_list[ing_info['ingredient_name']] = {'measure': ing_info['measure'], 'quantity': ing_info['quantity']}

        else:
            print(f'Ошибка! Блюда {dish} не существует в cookbook')
    for ingredient in shop_list:
        shop_list[ingredient]['quantity'] = shop_list[ingredient]['quantity'] * person
    return(shop_list)
menu(0)