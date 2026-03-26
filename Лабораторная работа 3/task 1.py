# TODO Напишите функцию для поиска индекса товара
def find_index(items_list, needed_item): #  Функция для поиска индекса первого вхождения товара в списке.
       # аргументы: items_list - список товаров, needed_item - нужный товар
       for index, item in enumerate(items_list): # Перебираем все элементы списка с помощью enumerate, чтобы получить индексы элементов
           if item == needed_item: # условие if: если элементы в списке является нужным товаром, то выводим индекс его первого вхождения
               return index
       return None # если нет товара нужного в списке, то выводим None

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_index(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")





