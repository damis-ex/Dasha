
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_quantity(self, quantity):
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} (Ціна: {self.price}$, В наявності: {self.quantity})"


class Cart:
    def __init__(self):
        self.items = {}

    def add_product(self, product, quantity):
        if product.name in self.items:
            self.items[product.name]['quantity'] += quantity
        else:
            self.items[product.name] = {'product': product, 'quantity': quantity}

    def remove_product(self, product):
        if product.name in self.items:
            del self.items[product.name]

    def calculate_total(self):
        total = 0
        for item in self.items.values():
            total += item['product'].price * item['quantity']
        return total

    def apply_discount(self, discount_percentage):
        total = self.calculate_total()
        discount = total * (discount_percentage / 100)
        return total - discount

    def show_cart(self):
        print("Ваша корзина:")
        for item in self.items.values():
            product = item['product']
            quantity = item['quantity']
            print(f"{product.name} - {quantity} шт. по ціні {product.price}$")

        print(f"Загальна сума: {self.calculate_total()}$")

    def clear_cart(self):
        self.items = {}


class Order:
    def __init__(self, cart, user):
        self.cart = cart
        self.user = user
        self.total_price = cart.calculate_total()

    def place_order(self):
        print(f"Замовлення на суму {self.total_price}$ оформлений для {self.user.name}.")


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.cart = Cart()


class Store:
    def __init__(self):
        self.products = {}
        self.orders = []

    def add_product(self, product):
        self.products[product.name] = product

    def remove_product(self, product_name):
        if product_name in self.products:
            del self.products[product_name]

    def list_products(self):
        print("Доступні товари:")
        for product in self.products.values():
            print(product)

    def find_product(self, product_name):
        return self.products.get(product_name, None)

    def create_order(self, user):
        order = Order(user.cart, user)
        self.orders.append(order)
        order.place_order()
        user.cart.clear_cart()

    def apply_discount(self, user, discount):
        total = user.cart.apply_discount(discount)
        print(f"Сума після використання знижки {discount}%: {total}$")


def main():
    store = Store()

    store.add_product(Product('Палетка ', 48, 10))
    store.add_product(Product('Масло для губ Dior', 40, 8))
    store.add_product(Product('Парфум Miss Dior', 150, 15))
    store.add_product(Product('Сяючий консилер', 15, 7))
    store.add_product(Product('Матуючий водостійкий спрей', 17, 25))
    store.add_product(Product('Кремовий бронзер', 20, 5))
    store.add_product(Product('Розсипчаста пудра', 47, 19))
    store.add_product(Product('Туш', 32, 1))

    name = input("Введіть ваше ім'я: ")
    email = input("Введіть ваш email: ")
    user = User(name, email)

    while True:
        print("\n1. Показати товари")
        print("2. Додавити товар в корзину")
        print("3. Показати корзину")
        print("4. Оформити замовлення")
        print("5. Застосувати знижку")
        print("6. Вихід")

        choice = input("Виберіть дію: ")

        if choice == '1':
            store.list_products()
        elif choice == '2':
            product_name = input("Введіть назву товару: ")
            product = store.find_product(product_name)
            if product:
                quantity = int(input(f"Скільки штук {product_name} додавити в корзину? "))
                if product.quantity >= quantity:
                    user.cart.add_product(product, quantity)
                    product.update_quantity(product.quantity - quantity)
                    print(f"{quantity} шт. {product_name} додано в корзину.")
                else:
                    print(f"Недостатньо товару на складі. В наявності тільки {product.quantity} шт.")
            else:
                print("Такого товару немає в магазині.")
        elif choice == '3':
            user.cart.show_cart()
        elif choice == '4':
            if user.cart.items:
                store.create_order(user)
            else:
                print("Ваша корзина порожня.")
        elif choice == '5':
            discount = int(input("Введіть розмір знижки (%): "))
            store.apply_discount(user, discount)
        elif choice == '6':
            print("Дякую за покупку! До побачення!")
            break
        else:
            print("Неправильний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
