
users = {
    'Марго': '11-15',
    'Софія': '5-10',
    'Інна': '35-44',
    'Арсеній': '18-24',
    'Артем': '55-64'
}

name = input("Введіть ім'я користувача: ")

if name in users:
    print(f"{name} належить до вікової групи: {users[name]}")
else:
    print(f"Ім'я {name} не знайдено у словнику.")
