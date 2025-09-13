
while True:
    try:
        number = int(input("Введіть число для таблиці множення: "))
        distance = int(input("Введіть число діапозону для таблиці: "))
        for i in range(1, distance + 1):
            result = number * i
            print(f"{number} x {i:2} = {result}")
        break
    except ValueError:
        print("Будь ласка, введіть дійсне ціле число.")

