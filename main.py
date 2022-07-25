cookbook_list = []
cook_book = {}
ingridients=[]
with open('files/cookbook.txt') as cookbook:
    for line in cookbook:
        cookbook_list.append(line.strip())
while len(cookbook_list) != 0:
    cook_book[cookbook_list[0]] = []
    for i in range (2, int(cookbook_list[1])+2):
        cook_book[cookbook_list[0]].append({'ingredient_name': cookbook_list[i].split(' | ')[0], 'quantity': int(cookbook_list[i].split(' | ')[1]), 'measure': cookbook_list[i].split(' | ')[2]})
    del cookbook_list[0:(int(cookbook_list[1])+3)]