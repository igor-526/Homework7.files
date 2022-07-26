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
        print('3. Получить отсортированный файл из файлов в папке for_sort')
        print('q. Выход из программы')
        choise = input('Выберите пункт: ')
        if choise == '1':
            print(cookbook())
            print()
        elif choise == '2':
            print(shoplist(input("Введите через запятую с пробелом наименования блюд: ").split(', '), int(input("Введите количество персон: "))))
            print()
        elif choise == '3':
            sorting()
            print()
        else:
            if choise != 'q':
                print('Вы выбрали несуществующий пункт меню! Попробуйте ещё раз!')
                print()
    else:
        print('До свидания!')
def shoplist(dishes, person):
    for i in range (0, len(dishes)):
        dishes[i] = dishes[i].capitalize()
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
def sorting():
    def getcounter(x):
        return(x['counter'])
    if os.path.isfile('result.txt'):
        os.remove('result.txt')
    ROOT_PATH = os.getcwd()
    FILE_DIR = 'for_sort'
    data_for_sort = []
    print(f'В папке для сортировки находится {len(os.listdir(path=os.path.join(ROOT_PATH, FILE_DIR)))} файла(-ов)')
    for file in os.listdir(path=os.path.join(ROOT_PATH, FILE_DIR)):
        with open(os.path.join(ROOT_PATH, FILE_DIR, file)) as file_for_sort:
            counter = 0
            for line in file_for_sort:
                counter+=1
        data_for_sort.append({'file': file, 'counter': counter})
    sorted_data = sorted(data_for_sort, key=getcounter)
    with open(os.path.join(ROOT_PATH, 'result.txt'), 'a') as sorted_file:
        for data_to_write in sorted_data:
            sorted_file.write(data_to_write['file'])
            sorted_file.write('\n')
            sorted_file.write(str(data_to_write['counter']))
            sorted_file.write('\n')
            with open(os.path.join(ROOT_PATH, FILE_DIR, data_to_write['file'])) as file_to_write:
                for line in file_to_write:
                    sorted_file.write(line)
                sorted_file.write('\n\n')
    print('Успешно! Отсортированный файл result.txt находится в папке с проектом')
menu(0)