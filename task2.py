def main():
    name = input("Введіть назву товару: ").strip()
    while not name:
        print("Назва товару не може бути порожньою.")
        name = input("Введіть назву товару: ").strip()

    while True:
        quantity_input = input("Введіть кількість проданих одиниць: ")
        try:
            quantity = int(quantity_input)
            if quantity < 0:
                print("Кількість не може бути від'ємною.")
                continue
            break
        except ValueError:
            print("Введіть ціле число для кількості.")

    while True:
        price_input = input("Введіть ціну за одиницю: ")
        try:
            price = float(price_input)
            if price < 0:
                print("Ціна не може бути від'ємною.")
                continue
            break
        except ValueError:
            print("Введіть число для ціни.")

    total = quantity * price
    print(f"Продукт: {name}, Кількість: {quantity}. Вартість: {total:.2f}")

if __name__ == "__main__":
    main()