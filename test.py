from classed import *


def dec(func):
    def wrapper(*args, **kwargs):
        print('-' * 30)
        result = func(*args, **kwargs)
        print('-' * 30)
        return result
    return wrapper


@dec
def info(store, shop):
    print('На складе:')
    [print(f'{k} - {v} шт.') for k, v in store.get_items.items()]
    print(f"Свободно: {store.get_free_space}\n{'-' * 30}\nВ магазине:")
    [print(f'{k} - {v} шт.') for k, v in shop.get_items.items()]
    print(f"Свободно: {shop.get_free_space}")


def ex_requests(reg_list, shop, store):
    for req in reg_list:
        print(req)
        if req.take_from is None:
            if store.add(req.product, req.amount):
                print('- выполнен')
            else:
                print('- не выполнен')
        elif req.take_from == 'store':
            if store.remove(req.product, req.amount):
                shop.add(req.product, req.amount)
                print('- выполнен')
            else:
                print('- не выполнен')
        elif req.take_from == 'shop':
            if shop.remove(req.product, req.amount):
                store.remove(req.product, req.amount)
                print('- выполнен')
            else:
                print('- не выполнен')


def main():
    my_store = Store({}, 100)
    my_shop = Shop({}, 20)
    requests_list = []
    while True:
        info(my_store, my_shop)
        print('[1] - Запрос\n[2] - Список запросов\n[3] - Очистить список\n[4] - Выполнить запросы\n'
              '\nMicrosoft Windows [Version 10.0.19042.1586]\n'
              '(c) Корпорация Майкрософт (Microsoft Corporation). Все права защищены.')
        option = input('\nC:\> ')

        if option == '1':
            print('Чтобы добавить продукты на склад, пропустите ввод "Откуда".\nВарианты ввода - shop, store')
            take_from = input('Откуда: ')
            replace_to = input('Куда: ')
            prod = input('Продукт: ')
            how_many = input('Колличество: ')
            if take_from:
                requests_list.append(Request(replace_to, int(how_many), prod, take_from))
            else:
                requests_list.append(Request(replace_to, int(how_many), prod))
        elif option == '2':
            for req in requests_list:
                print(f'---> {req}')
        elif option == '3':
            requests_list.clear()
        elif option == '4':
            ex_requests(requests_list, my_shop, my_store)
            requests_list.clear()
        else:
            print('Некорректный ввод')
            continue


if __name__ == '__main__':
    main()
