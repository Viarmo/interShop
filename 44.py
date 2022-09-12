print("Вас приветсвует Bank!")
mx = 100
s = mx
i = 0
print("Ваш баланс 100р")
while i < 1000 :
    i += 1
    prise = int(input("Введите сумму покупки"))
    if s > 0:
        s -= prise
        print("Ваш остаток на балансе", s)
    else:
        print("На вашем балансе недостаточно средств:", s)
