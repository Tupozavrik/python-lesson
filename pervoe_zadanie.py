def decor(func):
    def obertka(nach_skorost, final_skorost, time):
        try:
            nach_skorost = float(nach_skorost)
            final_skorost = float(final_skorost)
            time = float(time)
            if time == 0:
                raise ValueError("Время не может быть равно нулю.")
            uskorenie = func(nach_skorost, final_skorost, time)
            sr_skorost = (nach_skorost + final_skorost) / 2
            distance = sr_skorost * time
            print("Ускорение:", uskorenie)
            print("Пройденное расстояние:  м", distance)
            return uskorenie

        except ValueError:
            print(
                "Ошибка: время не равно нулю или вы ввели не число. Завершение программы."
            )

    return obertka


@decor
def calculate_uskorenie(nach_skorost, final_skorost, time):
    uskorenie = (final_skorost - nach_skorost) / time
    return uskorenie


print("введите начальную скорость")
a = input()
print("введите конечную скорость")
b = input()
print("введите время")
c = input()
calculate_uskorenie(a, b, c)
