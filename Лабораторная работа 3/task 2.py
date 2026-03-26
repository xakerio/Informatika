# TODO Напишите функцию find_common_participants
def find_common_participants(first_group,second_group, separator=","): # функция поиска общих участников
    #аргументы: first_group - первая группа, second_group - вторая группа, separator - разделитель
    set_first_group = set(first_group.split(separator)) # разбиваем строку первой группы на список с помощью split и преобразуем во множество
    set_second_group = set(second_group.split(separator)) # аналогично делаем со второй группой
    common_set = set_first_group.intersection(set_second_group) # находим пересечение множеств первой и второй группы
    common_list = list(common_set) # преобразуем множество общее в список
    common_list.sort() # сортируем список в алфавитном порядке
    return common_list

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

find_common_participants(participants_first_group,participants_second_group)
# TODO Провеьте работу функции с разделителем отличным от запятой

common_participants = find_common_participants(participants_first_group,participants_second_group, "|")
# вызываем функцию с другим разделителем | для проверки

print(f"Общие участники среди двух групп: {common_participants}")