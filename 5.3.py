def days():
    # Заданный кортеж с названиями дней недели
    days_of_week = ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье')

    # Запрашиваем у пользователя количество выходных дней
    while True:
        try:
            num_weekend_days = int(input("Сколько выходных дней на неделе вы хотите? (Введите число от 0 до 7): "))
            if 0 <= num_weekend_days <= 7:
                break
            else:
                print("Пожалуйста, введите число от 0 до 7.")
        except ValueError:
            print("Ошибка: введите целое число.")

    # Определяем выходные и рабочие дни
    weekend_days = days_of_week[-num_weekend_days:]  # Выходные дни с конца кортежа
    work_days = days_of_week[:-num_weekend_days] if num_weekend_days < 7 else []  # Рабочие дни

    # Выводим результат
    print("Ваши выходные дни:", ', '.join(weekend_days))
    print("Ваши рабочие дни:", ', '.join(work_days) if work_days else "Нет рабочих дней")

days()