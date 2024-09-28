
users_age_group = {
    "Олександра": "17-20",
    "Маріна": "10-15",
    "Микита": "25-30",
    "Дарія": "30-40",
    "Анна": "50-60"
}


def get_age_group():
    try:
        username = input("Введіть ім'я користувача: ")

        age_group = users_age_group[username]

        print(f"{username} належить до вікової групи: {age_group}")

    except KeyError:
        print("Користувача з таким ім'ям не знайдено.")

get_age_group()

