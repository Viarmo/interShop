print("Вас приветсвует Интернет магазин! Авторизуйтесь")
passvord = int(input("Введите пороль"))
while passvord == 1234:
    print("Добропожаловать Иван")
    print("Ваш баланс состовляет 100р")
    shop = int(input("выберите магазин: Канцелярия(1) / Продукты(2)"))
    if shop == 1:
        print("Добро пожаловать в концелярию")
        print("Посмотрите наши товары: \n Карандаши(1) \n Ручки(2) \n Тетради(3)")
        sum = 100
        pensils = 20
        pens = 40
        book = 90
        prise =  int(input("Выбериет товар: 1 2 3"))
        if sum:
            sum =-pensils
            print("покупка прошла успешно \n ваш остаток" ,sum)
        elif sum:
            sum =- pens
            print("покупка прошла успешно \n ваш остаток" ,sum)
        elif sum:
            sum =-book
            print("покупка прошла успешно \n ваш остаток",sum)
        else:
            print("у вас не достаточно средств")
    elif shop == 2:
        print("Добро пожаловать в продуктовый магазин")
        print("Посмотрите наши товары: \n Сахар \n Хлеб \n Молоко")
    else:
        print("Такого магазина я не знаю")
    break
else:
    print("Пороль не верный ")

