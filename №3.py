def check_age():
    try:
        age = int(input("Введіть свій вік: "))


        assert age >= 18, "Вам має бути 18 років або більше"


        print("Ви можете використовувати цей сервіс")
    except AssertionError as e:

        print(e)
    except ValueError:

        print("Будь ласка, введіть коректне число.")



check_age()
